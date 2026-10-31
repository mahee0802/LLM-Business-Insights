# LLM Business Insights

Turns raw e-commerce data into an executive-style business report. Pandas computes verified KPIs, and Gemini turns them into written analysis. Built on the Olist Brazilian e-commerce dataset (~100K orders, 2016-2018).

## How it works

```
Raw CSVs -> merge to order-item grain -> KPI summary (JSON) -> prompt builders -> Gemini -> reports
```

1. `src/data/build_business_dataset.py` merges 8 Olist tables into one analysis table
2. `src/analysis/generate_kpis.py` computes revenue, customer, order, product, payment, review, geography and seller KPIs
3. `src/llm/prompts.py` builds grounded prompts (currency, data coverage window, partial months)
4. `src/llm/generate_insights.py` calls Gemini with retry and backoff
5. `cli.py` (menu) and `app.py` (Streamlit) produce the reports in `outputs/`

## Setup

```bash
pip install pandas python-dotenv google-genai streamlit pytest
```

1. Download the [Olist dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) and put the CSVs in `data/raw/olist_dataset/`
2. Create a `.env` file:
   ```
   GEMINI_API_KEY=your_key
   GEMINI_MODEL=gemini-3.7-flash   # optional
   ```

## Run

```bash
python -m src.data.build_business_dataset   # build the merged table
python -m src.analysis.generate_kpis        # compute KPIs -> data/processed/business_summary.json
python cli.py                               # command-line report generator
streamlit run app.py                        # web UI
pytest -v                                   # tests
```

## Key results (Olist, Sep 2016 - Aug 2018)

- Revenue R$15.84M across 99,441 orders; AOV R$160.58
- 3.12% repeat purchase rate; SP generates 37% of revenue
- Average review 4.09; 11.5% of reviews are 1 star

## Engineering notes

Bugs found and fixed while validating the pipeline:

- **Join fan-out:** payments and reviews were joined onto item-level rows, inflating revenue from R$15.84M to R$16.64M. Fixed by aggregating payments and reviews to one row per order before joining, and covered by tests.
- **Wrong grain for order-level KPIs:** review counts and averages were computed on item rows (112,464 "reviews" vs 99,224 real). They now use one row per order.
- **LLM misreading data edges:** the model reported a "revenue collapse" in Sep/Oct 2018, which is just where the dataset ends. Prompts now state the currency, the coverage window and the partial months.

## Known limitations / next steps

- A Spark implementation exists in `src/spark/` but is not tested, and the reports use the pandas pipeline
- LLM output is not yet validated against the KPI JSON (a numeric claim checker is planned)
- Custom questions can only be answered from the KPI summary; tool calling over the dataset is planned

## Screenshots

<add a screenshot of the Streamlit app here>