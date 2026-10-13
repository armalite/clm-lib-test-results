import json
ctx=json.load(open('/task/workspace/context.json'))
ctx['entries']=[e for e in ctx['entries'] if e['id'].startswith('n')]
json.dump(ctx,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-11/board.md').read())
import glob
for f in sorted(glob.glob('/task/fixtures/round-11/logs/*')):
  for i,l in enumerate(open(f),1):
    if 'ERROR' in l or 'error' in l: print(f.split('/')[-1],i,l.strip()[:110])