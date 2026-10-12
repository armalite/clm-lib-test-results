import json,re,glob
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR5: board follow-up OPEN VENDOR_TICKET (round-05/board.md:3).'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|WARN|429|batch|miss|disk|used_pct',l,re.I): print(f.split('/')[-1],i,l.strip()[:150])