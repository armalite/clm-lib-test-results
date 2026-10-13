import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Q1 DONE: 375 EUR cite HB-62 §2, HB-24 §2, HB-24 §3. Q2 DONE: 250 EUR cite HB-64 §2, HB-53 §2 (carve-out HB-53 §3 contractors only, n/a).'}]}
json.dump(c,open('/task/workspace/context.json','w'))