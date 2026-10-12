import json
t=open('/task/fixtures/round-07/changes.md').read();print(t)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
for x in c['entries']:
  if x['id']=='n7': x['body']=x['body'].replace('no changes.md checked? (board empty)','changes.md: '+' | '.join(l for l in t.splitlines() if 'CHG' in l)[:400])
json.dump(c,open('/task/workspace/context.json','w'))