import json
b=open('/task/workspace/context.json').read()
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]['body']
n=n.replace('\nNext: advance to round 5.','\nR5: board empty; CHG-140 log sampling (noise). dns continues auth (round-05/logs/auth-svc.log:1,12,19) checkout (round-05/logs/checkout-api.log:2,7,8); search 429 fx-rates (round-05/logs/search-api.log:5,19,20,33). inventory/shipping clean.\nNext: advance to round 6.')
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')