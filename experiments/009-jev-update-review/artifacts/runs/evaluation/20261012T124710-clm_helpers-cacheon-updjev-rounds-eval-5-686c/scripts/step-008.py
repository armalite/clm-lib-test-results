import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]['body']
n+='\nR3 logs: auth-svc shows tls certificate_expired peer=bank-api (round-03/logs/auth-svc.log:1,16,21,25,35,62), no memory evidence -> real cause likely CERT_EXPIRED, board says MEMORY_LEAK. No checkout errors R3.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))
print('ok')