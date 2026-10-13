import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Q1: 375 EUR cites HB-62 §2, HB-24 §2, HB-24 §3. Q2: 250 EUR cites HB-64 §2, HB-53 §2. Q3: 29 EUR cites HB-70 §2 (superseded version valid 2025-06-01..2026-02-28; daytime so HB-37 night exception n/a). Next: Q4 parental leave, Q5 relocation, Q6 parking.'}]}
json.dump(c,open('/task/workspace/context.json','w'))