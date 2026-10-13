import json,re
L=open('/task/fixtures/round-10/logs/shipping-svc.log').read().splitlines()
h=[i+1 for i,l in enumerate(L) if 'config validation failed' in l]
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]['body']
n=n.replace('\nNext: advance to round 10.','\nR10: board Thread C note pods restarting, investigation continues (round-10/board.md:3); Follow-up CLOSED ALERT_TUNING (board.md:4). shipping config validation failed (round-10/logs/shipping-svc.log:'+','.join(map(str,h[:6]))+'). inventory 429 (round-10/logs/inventory-svc.log:36,59); search 429 (round-10/logs/search-api.log:13,31). auth/checkout clean.\nNext: advance to round 11.')
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))
print(h)