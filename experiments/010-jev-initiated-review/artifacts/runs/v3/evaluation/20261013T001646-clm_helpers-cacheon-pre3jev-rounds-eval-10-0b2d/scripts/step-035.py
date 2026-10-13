import json,re
L=open('/task/fixtures/round-09/logs/shipping-svc.log').read().splitlines()
h=[i+1 for i,l in enumerate(L) if 'config validation failed' in l]
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]['body']
n=n.replace('\nNext: advance to round 9.','\nR9: board Thread C opened shipping-svc failures cause unknown ongoing (round-09/board.md:3); follow-ups OPEN RUNBOOK_UPDATE (board.md:4), CUSTOMER_COMMS (board.md:5). shipping ERROR config validation failed retry.backoff_ms=0 -> BAD_CONFIG_ROLLOUT from CHG-113 (round-09/logs/shipping-svc.log:'+','.join(map(str,h[:6]))+'). inventory 429 (round-09/logs/inventory-svc.log:66,67); search 429 (round-09/logs/search-api.log:12,14). auth/checkout clean.\nNext: advance to round 10.')
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))
print(h)