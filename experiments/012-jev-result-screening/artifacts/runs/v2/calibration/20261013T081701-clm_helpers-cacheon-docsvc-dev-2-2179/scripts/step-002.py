import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Q1: daytime taxi = 42 EUR (HB-38 §2 current from 2026-03-01; HB-01 §2 night 22-06 =70 not applicable; HB-38 §3 trade fair luggage +23 not applicable). Next: Q2 home office 2026-03-15.'}]}
json.dump(c,open('/task/workspace/context.json','w'))