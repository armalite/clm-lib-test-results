import json
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'All 4 stages released; 14/14 visible tests pass at step 9. core.py reviewed step 10: region tax NZ15/AU10/US0/else12 (0 if tax_exempt is True); tiers gold5/silver2; bulk >=200 x0.88, >=50 x0.95; validation; half-even rounding of exact sub/disc/tax; format_money with comma separators. Remaining: check stage-1 format_money spec text.'}]},open('/task/workspace/context.json','w'))
s=open('/task/fixtures/stage-1/REQUIREMENTS.md').read()
i=s.find('## Rules');print(s[i+150:i+1500])