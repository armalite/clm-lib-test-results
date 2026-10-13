import json,re
print(open('/task/fixtures/round-11/board.md').read())
import glob
for f in sorted(glob.glob('/task/fixtures/round-11/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search('ERROR|429|dns|config|heap',l): print(f.split('/')[-1],i,l.strip()[:150])
ctx=json.load(open('/task/workspace/context.json'))
ctx['entries']=[e for e in ctx['entries'] if e['id']=='n1']
json.dump(ctx,open('/task/workspace/context.json','w'))