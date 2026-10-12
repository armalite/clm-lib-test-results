import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR8 logs: auth cert_expired (round-08/logs/auth-svc.log:6,83); checkout quiet in R8 (pool issue may have stopped).'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')