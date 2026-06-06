import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
raw = pd.read_csv(ROOT / 'data/raw_customer_orders.csv')

clean = raw.copy()
clean['email'] = clean['email'].fillna('').str.strip().str.lower()
clean['phone'] = clean['phone'].astype(str).str.replace(r'\D+', '', regex=True)
clean['city'] = clean['city'].fillna('Unknown').str.strip().str.lower()
city_map = {'moscow':'Moscow','москва':'Moscow','saint petersburg':'Saint Petersburg','spb':'Saint Petersburg','tallin':'Tallinn','tallinn':'Tallinn','riga':'Riga','berlin':'Berlin','unknown':'Unknown'}
clean['city'] = clean['city'].map(city_map).fillna(clean['city'].str.title())
clean['status'] = clean['status'].fillna('').str.strip().str.lower().replace({'оплачен':'paid','canceled':'cancelled'})
clean['amount'] = clean['amount'].astype(str).str.replace(',', '.', regex=False).astype(float)
clean['order_date'] = pd.to_datetime(clean['order_date'], errors='coerce', dayfirst=False)
clean['month'] = clean['order_date'].dt.to_period('M').astype(str)
clean = clean.drop_duplicates(subset=['order_id','customer_name','product','amount'])

summary = pd.DataFrame({
    'metric':['raw_rows','clean_rows','duplicates_removed','missing_email_after_clean','total_revenue_paid','paid_orders'],
    'value':[len(raw), len(clean), len(raw)-len(clean), int((clean['email']=='').sum()), round(clean.loc[clean.status=='paid','amount'].sum(),2), int((clean.status=='paid').sum())]
})

(ROOT / 'results').mkdir(exist_ok=True)
clean.to_csv(ROOT / 'results/clean_customer_orders.csv', index=False)
summary.to_csv(ROOT / 'results/cleaning_summary.csv', index=False)

monthly = clean[clean.status=='paid'].groupby('month', as_index=False)['amount'].sum()
plt.figure(figsize=(8,4))
plt.plot(monthly['month'], monthly['amount'], marker='o')
plt.title('Paid revenue after data cleaning')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(ROOT / 'results/revenue_after_cleaning.png', dpi=160)

print(summary.to_string(index=False))
