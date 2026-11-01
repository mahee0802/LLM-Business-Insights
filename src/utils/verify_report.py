"""
Numeric claim checker.

Extracts every number from a generated report and checks whether it can be traced
to the KPI summary: either directly (a KPI value) or as a simple derived figure
(a share of a total, or the repeat-customer rate). Anything else is flagged for
manual review. This does not prove a report is correct, but it catches invented
or mistyped numbers cheaply.
"""
import json
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
SUMMARY_PATH = BASE_DIR / "data" / "processed" / "business_summary.json"
OUTPUTS_DIR = BASE_DIR / "outputs"

HEX_ID = re.compile(r"\b[0-9a-f]{32}\b")
LIST_MARKER = re.compile(r"^\s*(?:#+\s*)?\d+[.)]\s", re.MULTILINE)
YEAR_MONTH = re.compile(r"\b(?:19|20)\d{2}-\d{2}\b")
NUMBER = re.compile(r"(?<![\w.])(\d{1,3}(?:,\d{3})+|\d+)(\.\d+)?\s?(%|[MK]\b)?")


def _numbers_in(obj):
    """Yield every numeric value found in a nested JSON structure."""
    if isinstance(obj, dict):
        for value in obj.values():
            yield from _numbers_in(value)
    elif isinstance(obj, list):
        for value in obj:
            yield from _numbers_in(value)
    elif isinstance(obj, (int, float)) and not isinstance(obj, bool):
        yield float(obj)


def _numeric_dicts(obj, found=None):
    """Collect every dict whose values are all numbers (breakdowns by state, category, ...)."""
    if found is None:
        found = []
    if isinstance(obj, dict):
        if obj and all(isinstance(v, (int, float)) and not isinstance(v, bool) for v in obj.values()):
            found.append(obj)
        for value in obj.values():
            _numeric_dicts(value, found)
    elif isinstance(obj, list):
        for value in obj:
            _numeric_dicts(value, found)
    return found


def build_candidates(summary):
    """
    Returns (plain, percent): the values a report number may legitimately match.
    plain   = KPI values, sums of leading/trailing groups, ratios between matching breakdowns
    percent = KPI percentages and shares of totals
    """
    plain = set(_numbers_in(summary))
    percent = set()

    totals = [
        summary["revenue"]["total_revenue"],
        summary["orders"]["total_orders"],
        summary["customers"]["total_customers"],
    ]
    customers = summary["customers"]
    repeat_rate = customers["repeat_customers"] / customers["total_customers"] * 100
    percent.update([repeat_rate, 100 - repeat_rate, summary["orders"]["delayed_order_percentage"]])
    plain.add(customers["total_customers"] - customers["repeat_customers"])

    dicts = _numeric_dicts(summary)
    for mapping in dicts:
        values = list(mapping.values())
        # leading and trailing groups (top-3 states, 1-2 stars, 4-5 stars, ...)
        groups = [sum(values[:k]) for k in range(1, len(values) + 1)]
        groups += [sum(values[-k:]) for k in range(1, len(values) + 1)]
        if len(values) <= 30:  # any run of adjacent items (e.g. canceled + unavailable)
            groups += [
                sum(values[i:j])
                for i in range(len(values))
                for j in range(i + 2, len(values) + 1)
            ]
        plain.update(groups)
        for amount in values + groups:
            for denominator in totals + [sum(values)]:
                if denominator:
                    percent.add(amount / denominator * 100)

    # ratios between breakdowns that share keys (revenue per order, per state, per category)
    for a in dicts:
        for b in dicts:
            if a is b:
                continue
            for key in a.keys() & b.keys():
                if b[key]:
                    plain.add(a[key] / b[key])

    percent.update(100 - p for p in list(percent))  # complements ("other states" = 100 - top states)
    return plain, percent


def extract_claims(text):
    """Return (shown_value, decimals, scale, is_percent, snippet) for each checkable number."""
    cleaned = HEX_ID.sub(" ", text)
    cleaned = YEAR_MONTH.sub(" ", cleaned)
    cleaned = LIST_MARKER.sub(" ", cleaned)
    claims = []
    for match in NUMBER.finditer(cleaned):
        whole, frac, suffix = match.group(1), match.group(2), match.group(3)
        digits = whole.replace(",", "")
        decimals = len(frac) - 1 if frac else 0
        value = float(digits + (frac or ""))
        # skip calendar years and small bare integers (counts like "top 5")
        if not frac and not suffix and "," not in whole:
            if 1900 <= value <= 2100 or value <= 10:
                continue
        scale = {"M": 1e6, "K": 1e3}.get(suffix, 1)
        start = max(0, match.start() - 40)
        snippet = cleaned[start:match.end() + 20].replace("\n", " ").strip()
        claims.append((value, decimals, scale, suffix == "%", snippet))
    return claims


def is_supported(value, decimals, scale, is_percent, plain, percent):
    # decimals may differ by one unit in the last digit (models often truncate instead of round);
    # whole numbers must match exactly
    tolerance = 10 ** (-decimals) + 1e-9 if decimals else 0.5
    pool = percent if is_percent else plain
    return any(abs(candidate / scale - value) <= tolerance for candidate in pool)


def verify_text(text, summary):
    plain, percent = build_candidates(summary)
    claims = extract_claims(text)
    unsupported = [
        c[4] for c in claims if not is_supported(c[0], c[1], c[2], c[3], plain, percent)
    ]
    return len(claims), unsupported


def main():
    # reports contain non-ASCII characters; avoid Windows console encoding errors
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    with open(SUMMARY_PATH, encoding="utf-8") as f:
        summary = json.load(f)

    reports = sorted(OUTPUTS_DIR.glob("*.md"))
    if not reports:
        print("No reports found in outputs/")
        return 1

    for path in reports:
        text = path.read_text(encoding="utf-8")
        total, unsupported = verify_text(text, summary)
        verified = total - len(unsupported)
        pct = verified / total * 100 if total else 100
        print(f"\n{path.name}: {verified}/{total} numbers traced to KPIs ({pct:.0f}%)")
        for snippet in unsupported:
            print(f"   ? ...{snippet}...")
    return 0


if __name__ == "__main__":
    sys.exit(main())