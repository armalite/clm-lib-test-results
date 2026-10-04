import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' Stage2: changes.log:1 CHG-5117 APPLIED risk-score timeout 3500 (mitigated). oncall says db pool exhaustion now. stage-2 gateway 503 line 58.'
json.dump(c,open('/task/workspace/context.json','w'))
b='/task/fixtures/stage-2/logs/quotes-api.log'
n=0
for i,l in enumerate(open(b),1):
  if 'pool' in l:
    n+=1
    if n<3:print(i,l.strip()[:180])
print(n)