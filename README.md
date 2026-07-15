# LLM Business Insights Pipeline
An end-to-end LLM-powered Business Insights Pipeline that analyzes an e-commerce dataset, generates business KPIs, and uses Google's Gemini API to produce professional business reports and answer business questions through dynamic prompt engineering.

---

## Project Overview

This project demonstrates how Large Language Models (LLMs) can be integrated into a traditional data analytics workflow.

The pipeline:

- Loads processed business data
- Generates key business metrics (KPIs)
- Stores them in a structured JSON format
- Uses prompt engineering techniques to build dynamic prompts
- Sends prompts to the Gemini API
- Generates professional business reports
- Saves reports as Markdown files

The project emphasizes clean architecture, modular design, prompt engineering, and reusable LLM workflows.

---

## Features

### Data Processing

- Load processed business data
- Generate business KPIs
- Save KPIs as a structured JSON file

### LLM Integration

- Google Gemini API integration
- Modular LLM client
- Dynamic prompt generation

### Business Analysis

Generate:

- Full Business Report
- Revenue Analysis
- Customer Analysis
- Product Analysis
- Custom Business Question Analysis

### Prompt Engineering

Implements:

- Role Prompting
- Prompt Templates
- Zero-shot Prompting
- Dynamic Prompt Generation
- Modular Prompt Functions

### Report Generation

Reports are generated in Markdown format and automatically saved inside the `outputs/` folder.

---

## Project Structure

```text
LLM_Pipeline/

│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│
├── notebooks/
│
├── outputs/
│   ├── business_report.md
│   ├── revenue_report.md
│   ├── customer_report.md
│   ├── product_report.md
│   └── custom_question.md
│
├── src/
│   │
│   ├── analysis/
│   │   └── generate_kpis.py
│   │
│   ├── data/
│   │   └── load_data.py
│   │
│   ├── llm/
│   │   ├── llm_client.py
│   │   ├── prompts.py
│   │   └── generate_insights.py
│   │
│   └── utils/
│       └── save_report.py
│
├── app.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## Technologies Used

### Programming Language

- Python

### Libraries

- Pandas
- NumPy
- python-dotenv
- Google GenAI SDK

### LLM

- Google Gemini 2.5 Flash

### Development Tools

- VS Code
- Git
- GitHub

---

## Dataset

This project uses the **Brazilian E-Commerce Public Dataset by Olist**.

The current version of the project utilizes selected datasets to generate business insights.

Examples include:

- Orders
- Order Items
- Customers

The project is designed to support additional Olist datasets in future iterations.

---

## Workflow

```text
Processed Dataset
        │
        ▼
Generate Business KPIs
        │
        ▼
business_summary.json
        │
        ▼
Prompt Builder
        │
        ▼
Gemini API
        │
        ▼
Business Report
        │
        ▼
Markdown Report
```

---

## Prompt Engineering Workflow

```text
Business Summary
        │
        ▼
Prompt Template
        │
        ▼
Selected Analysis Type
        │
        ▼
Dynamic Prompt
        │
        ▼
Gemini API
        │
        ▼
Generated Report
```

---

## Available Analyses

When the application starts, users can choose one of the following:

```
1. Generate Full Business Report
2. Revenue Analysis
3. Customer Analysis
4. Product Analysis
5. Ask a Custom Business Question
0. Exit
```

Each option generates a different prompt and produces a specialized report.

---

## Example Business Report Sections

A full report typically contains:

- Executive Summary
- Revenue Analysis
- Customer Behavior Insights
- Product Performance
- Potential Business Risks
- Growth Opportunities
- Actionable Recommendations

---

## Installation

Clone the repository

```bash
git clone <repository-url>
```

Move into the project directory

```bash
cd LLM_Pipeline
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the virtual environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file inside the project root.

Example:

```text
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Running the Project

Run

```bash
python app.py
```

Select the desired analysis from the interactive menu.

The generated report will be displayed in the terminal and saved inside the `outputs/` directory.

---

## Example Output

```
========================================
BUSINESS INSIGHTS GENERATOR
========================================

1. Generate Full Business Report
2. Revenue Analysis
3. Customer Analysis
4. Product Analysis
5. Ask a Custom Business Question
0. Exit
========================================
```

---

## Learning Outcomes

This project demonstrates practical understanding of:

- Data preprocessing
- Business KPI generation
- JSON-based data exchange
- API integration
- Google Gemini API
- Prompt Engineering
- Dynamic Prompt Templates
- Modular Software Design
- Command Line Applications
- Git and GitHub

---

## Future Improvements

Potential enhancements include:

- Integration of additional Olist datasets
- Richer business KPI generation
- Advanced business analytics
- Retrieval-Augmented Generation (RAG)
- Streamlit web application
- Interactive dashboards
- Report versioning with timestamps
- JSON structured LLM outputs

---

## Author

**Mahee Patkar**

Engineering Student | AI & Machine Learning Enthusiast

---

## License

This project is intended for educational and portfolio purposes.