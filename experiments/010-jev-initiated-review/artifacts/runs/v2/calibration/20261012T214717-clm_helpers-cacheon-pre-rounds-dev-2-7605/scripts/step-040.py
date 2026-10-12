import json
t=open('/task/workspace/spill/s38.obs.txt').read()
print(t[:2600])
ctx=json.load(open('/task/workspace/context.json'))
ctx['entries']=[e for e in ctx['entries'] if e['id']=='n1']
json.dump(ctx,open('/task/workspace/context.json','w'))