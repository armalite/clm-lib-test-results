import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Q1: 375 EUR cites HB-62 §2, HB-24 §2, HB-24 §3. Q2: 250 EUR cites HB-64 §2, HB-53 §2. Q3: 29 EUR cites HB-70 §2. Q4: 12 weeks cites HB-06 §2, HB-71 §2, HB-71 §3 (carve-out first year). Next: Q5 relocation, Q6 parking.'}]}
json.dump(c,open('/task/workspace/context.json','w'))