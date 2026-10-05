import json,glob,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
json.dump(c,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-11/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-11/logs/*')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|error|SERVFAIL|expired|invalid|config',l): print(f.split('/')[-1],i,l.strip()[:150])