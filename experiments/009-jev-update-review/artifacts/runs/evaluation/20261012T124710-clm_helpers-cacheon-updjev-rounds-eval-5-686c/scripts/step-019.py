import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]['body']
n+="\nR7 logs: checkout db pool exhausted (round-07/logs/checkout-api.log:2,8,33,38,47); auth tls handshake failed peer=bank-api (round-07/logs/auth-svc.log:12,21,24,29). NEXT: advance to R8."
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))
print('ok')