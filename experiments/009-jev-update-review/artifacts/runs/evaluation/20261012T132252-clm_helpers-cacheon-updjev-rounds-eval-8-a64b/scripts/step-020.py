import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if not e['id'].startswith('s19')]
json.dump(c,open('/task/workspace/context.json','w'))
print(len(c['entries']))