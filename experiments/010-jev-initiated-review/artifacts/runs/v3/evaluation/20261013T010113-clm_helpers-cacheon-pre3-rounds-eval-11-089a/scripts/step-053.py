import json
s=open('/task/workspace/spill/s51.obs.txt').read()
print(s[:2500])
for f in ['board.md','changes.md']:
  try:
    for i,l in enumerate(open('/task/fixtures/round-10/'+f),1): print(f,i,l.rstrip()[:160])
  except Exception as e: print(e)
ctx=json.load(open('/task/workspace/context.json'))
ctx['entries']=[e for e in ctx['entries'] if e['id'].startswith('n')]
ctx['entries'].append({'id':'n10','role':'note','body':'Round10: see spill/s51.obs.txt for log summary; round-10 board/changes printed at step 53 (check obs). Next: record n10 details then advance.'})
json.dump(ctx,open('/task/workspace/context.json','w'))