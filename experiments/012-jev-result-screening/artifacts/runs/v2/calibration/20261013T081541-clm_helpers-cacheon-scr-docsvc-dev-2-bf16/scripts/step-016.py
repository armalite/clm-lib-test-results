import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Q1 done: 42 EUR [HB-38 §2]. Q2 done: 350 EUR [HB-16 §2]. Q3 done: 450 EUR [HB-56 §2, HB-56 §3]. Q4 done: 75 EUR [HB-33 §2, HB-34 §2, HB-34 §3]. Q5 done: 250 EUR [HB-31 §2, HB-53 §2]. Next: Q6 bike leasing e-bike + insurance.'}]}
json.dump(c,open('/task/workspace/context.json','w'))