import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Q1: 375 EUR (16h<20h carve-out) cites HB-62 §2, HB-24 §2, HB-24 §3. SR-001 omitted HB-48 §1 (check maybe).'}]}
json.dump(c,open('/task/workspace/context.json','w'))