from src.utils.verify_report import verify_text

SUMMARY = {
    "revenue": {"total_revenue": 1000.0, "average_order_value": 100.0},
    "orders": {"total_orders": 10, "delayed_order_percentage": 6.5},
    "customers": {"total_customers": 8, "repeat_customers": 1},
    "reviews": {"rating_distribution": {"1": 2, "2": 1, "3": 3, "4": 2, "5": 2}},
}


def test_kpi_values_are_verified():
    text = "Revenue was R$ 1,000.00 with an AOV of R$ 100.00; 6.5% of orders were late."
    total, unsupported = verify_text(text, SUMMARY)
    assert total == 3
    assert unsupported == []


def test_invented_number_is_flagged():
    total, unsupported = verify_text("Revenue was R$ 1,234.56 last year.", SUMMARY)
    assert total == 1
    assert len(unsupported) == 1


def test_derived_share_is_verified():
    # 1-star + 2-star reviews = 3 of 10 = 30.0%
    total, unsupported = verify_text("30.0% of reviews were 1 or 2 stars.", SUMMARY)
    assert total == 1
    assert unsupported == []


def test_wrong_count_is_flagged():
    total, unsupported = verify_text("There were 98,665 reviews.", SUMMARY)
    assert len(unsupported) == 1


def test_years_ids_and_small_counts_are_ignored():
    text = "In 2017 the top 5 sellers (4869f7a5dfa277a7dca6462dcf3b52b2) grew."
    total, unsupported = verify_text(text, SUMMARY)
    assert total == 0