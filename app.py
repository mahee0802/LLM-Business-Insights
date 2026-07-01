from src.data.load_data import load_business_summary
from src.llm.prompts import build_prompt
from src.llm.generate_insights import generate_business_report
from src.utils.save_report import save_report


def main():

    business_summary = load_business_summary()

    prompt = build_prompt(business_summary)

    report = generate_business_report(prompt)

    print(report)

    save_report(report)


if __name__ == "__main__":
    main()