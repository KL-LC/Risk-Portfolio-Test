import pandas as pd, numpy as np, os
os.makedirs('docs/data', exist_ok=True)

# Tiny placeholder datasets (content is not important)
dates = pd.date_range('2024-01-01', periods=6, freq='MS')
seg = pd.DataFrame({
    'asof_date': dates,
    'region': ['NSW','VIC','QLD','WA','SA','NSW'],
    'pd_avg': [0.012,0.014,0.013,0.016,0.015,0.017],
    'lgd_avg': [0.30,0.31,0.29,0.32,0.30,0.31],
    'ecl_total': [120000, 135000, 128000, 150000, 142000, 160000],
    'accounts': [100,110,105,120,115,125],
})
seg.to_csv('docs/data/segment_agg.csv', index=False)

acct = pd.DataFrame({
    'asof_date': [dates[-1]]*10,
    'loan_id': range(100001,100011),
    'region': np.random.choice(['NSW','VIC','QLD','WA','SA'], size=10),
    'PD': np.round(np.random.uniform(0.005, 0.15, size=10), 4),
    'LGD': np.round(np.random.uniform(0.15, 0.6, size=10), 2),
    'EAD': np.round(np.random.uniform(50000, 500000, size=10), 0),
    'Score': np.round(np.random.normal(620, 40, size=10), 0)
})
acct['ECL'] = (acct['PD']*acct['LGD']*acct['EAD']).round(2)
acct.to_csv('docs/data/account_scores.csv', index=False)

watch = acct.sort_values('PD', ascending=False).head(5)
watch.to_csv('docs/data/watchlist_top.csv', index=False)

print('Wrote docs/data/*.csv')
