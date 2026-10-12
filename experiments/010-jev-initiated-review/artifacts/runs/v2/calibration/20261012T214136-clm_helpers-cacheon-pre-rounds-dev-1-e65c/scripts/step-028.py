import json
d=json.load(open('/task/workspace/context.json'))
b=[e for e in d['entries'] if e['id']=='n1'][0]['body']
b=b.replace(' Next: advance to round 7.','')
b+='\nRound7: board empty (no changes). no changes.md. checkout-api 429 fx-rates 11..66; payments-svc 429 1..82; auth/search/notify clean. Next: advance to round 8.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':b}]},open('/task/workspace/context.json','w'))
print('ok')