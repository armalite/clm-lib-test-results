import json,re
for s in ['checkout-api','auth-svc']:
    L=open(f'/task/fixtures/round-08/logs/{s}.log').read().splitlines()
    h=[(i+1,l[:140]) for i,l in enumerate(L) if re.search('ERROR|WARN',l) and 'slow' not in l]
    print(s,len(h));[print(x) for x in h[:4]]
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']=n['body'].replace(' Next: advance to R8.','')+'\nR8: board.md:3 Thread D closed as false alarm (synthetic monitor), BUT R6-7 logs showed real pool exhaustion; verify with logs. changes.md:3 CHG-156 PROPOSED (ignore).'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))