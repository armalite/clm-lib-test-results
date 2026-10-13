import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Q1: 375 EUR cites HB-62 §2, HB-24 §2, HB-24 §3 (HB-48 irrelevant). Q2: 250 EUR cites HB-64 §2, HB-53 §2 (HB-53 §3 contractors only, not relevant). Next: Q3 taxi 2026-02-15, Q4, Q5, Q6.'}]}
json.dump(c,open('/task/workspace/context.json','w'))