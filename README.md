# Python Data Cleaning & Quality Report

    **Role:** Data Analyst / Python Analyst  
    **Dataset:** Synthetic / anonymized demo data created for portfolio use.  
    **Stack:** Python, pandas, matplotlib, CSV/Excel processing

    ## Business problem

    Raw customer order data contained duplicate rows, inconsistent date formats, text-based numeric values, mixed city names, missing emails, and inconsistent order statuses.

    ## What was built

    Built a reproducible Python/pandas cleaning pipeline that standardizes emails, phones, cities, dates, statuses and revenue fields; removes duplicates; exports clean data and a quality summary report.

    ## Key outputs

    - `results/clean_customer_orders.csv` — cleaned dataset
- `results/cleaning_summary.csv` — data quality metrics
- `results/revenue_after_cleaning.png` — visual trend after cleaning

    ## How to run

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Windows: .venv\Scripts\activate
    pip install -r requirements.txt
    python src/main.py
    ```

    ## Resume-ready bullets

    - Automated cleaning of a messy customer-order dataset using Python/pandas: standardized dates, emails, phones, statuses and revenue fields.
- Removed duplicates and generated a reusable data-quality report with clean CSV export and revenue visualization.
