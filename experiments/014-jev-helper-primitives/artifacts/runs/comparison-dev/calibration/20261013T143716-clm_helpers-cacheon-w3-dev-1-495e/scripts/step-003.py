import json
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries']=[e for e in c['entries'] if e['id'] in('register','status')]
json.dump(c,open(p,'w'))
print('ok')