import json
t=open('/task/workspace/spill/s19.obs.txt').read()
print(t[:2500])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))