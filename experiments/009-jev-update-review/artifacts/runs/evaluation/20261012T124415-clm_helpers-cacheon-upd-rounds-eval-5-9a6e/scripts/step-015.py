import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+=' R5 logs: auth-svc certificate_expired bank-api round-05/logs/auth-svc.log:1,3,13,75; no disk errors seen. Next: advance R6.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))