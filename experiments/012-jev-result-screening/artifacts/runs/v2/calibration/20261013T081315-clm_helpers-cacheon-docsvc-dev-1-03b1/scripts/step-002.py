import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Q1 DONE: 375 EUR (16h<20 carve-out -> standard HB-62 §2 current since 2026-05-01). cite HB-62 §2, HB-24 §2, HB-24 §3.'}]}
json.dump(c,open('/task/workspace/context.json','w'))