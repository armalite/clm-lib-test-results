import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]['body']
n+='\nR6 logs: checkout 'db pool exhausted' (round-06/logs/checkout-api.log:8,25,27,34,42); auth errors continue (round-06/logs/auth-svc.log:2,31-37). Search/shipping disk quiet R6.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))
print('ok')