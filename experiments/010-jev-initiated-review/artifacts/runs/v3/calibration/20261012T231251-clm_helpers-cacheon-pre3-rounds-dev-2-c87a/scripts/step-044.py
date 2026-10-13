import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']=n['body'].replace(' Next: advance to round 9.','')+' R9: Thread C note pods restarting (round-09/board.md:3). CHG-166 retry budget (noise). Cert logs round-09/logs/auth-svc.log:22,55; shipping-svc.log:28,56. search-api config fail round-09/logs/search-api.log:2, 429 :1,5. Next: advance to round 10.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')