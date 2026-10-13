import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Q1: 42 EUR (HB-38 §2). Q2: 350 EUR (HB-16 §2 superseded version effective 2025-03-01..2026-03-31; HB-63 400 from 2026-04-01; HB-46 memo group exceptions, regular employee = standard). Next: Q3 flight fare Europe checked equipment.'}]}
json.dump(c,open('/task/workspace/context.json','w'))