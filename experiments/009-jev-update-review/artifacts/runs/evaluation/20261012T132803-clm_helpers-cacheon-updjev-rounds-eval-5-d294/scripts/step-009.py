import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
    L=open(f).read().splitlines()
    errs=[(i+1,l[:130]) for i,l in enumerate(L) if re.search('ERROR|disk|pool|certificate',l)]
    print(f.split('/')[-1],len(errs))
    for e in errs[:3]+errs[-2:]: print(' ',e)
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR4: board.md:3 Thread A mitigated (after changes.md:4 CHG-136 APPLIED search-api mitigation); board.md:4 OPEN DATA_BACKFILL; :5 OPEN VENDOR_TICKET. CHG-131 PROPOSED (ignore).'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))