import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id']=='n1']
e[0]['body']+='\nR6 logs: ledger-svc heap rss_mb high round-06/logs/ledger-svc.log:2,6,14,35,45,52 (memory leak confirmed); payments disk used_pct continues round-06/logs/payments-svc.log:3,16,30,36,83.'
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')