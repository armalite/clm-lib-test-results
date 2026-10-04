import json
b='/task/fixtures/stage-2/'
L=open(b+'logs/payments-api.log').read().splitlines()
c=0
for i,l in enumerate(L,1):
  if 'ERROR' in l and 'tax-engine' not in l:
    print(i,l[:200]);c+=1
    if c>3:break
ctx=json.load(open('/task/workspace/context.json'))
n=[e for e in ctx['entries'] if e['id']=='n1'][0]
n['body']+=' Stage2: changes.log:1 CHG-5266 APPLIED tax timeout=4000 (fixes timeout). changes.log:2 PROPOSED ignore. oncall stage2 notes:6 suspects db pool exhaustion but yaml 48 (yaml overridden by release notes 10). metrics db_pool_in_use col. ingress-a stage2 503 line53.'
ctx['entries']=[n]
json.dump(ctx,open('/task/workspace/context.json','w'))