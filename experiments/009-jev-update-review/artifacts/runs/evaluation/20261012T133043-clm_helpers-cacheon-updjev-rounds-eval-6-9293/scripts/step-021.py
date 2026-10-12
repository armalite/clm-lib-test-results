import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
    L=open(f).read().splitlines()
    hits=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|WARN|429|heap|disk|cert|DNS|lag|pool|cache',l,re.I) and 'slow' not in l.lower()]
    print(f.split('/')[-1],len(hits),hits[:15])
    if hits: print(' ',L[hits[0]-1][:160])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']=c['entries'][0]['body'].replace(' Next: advance to R7.','')+' R7: board.md:3 Thread A RESOLVED; board.md:4 OPEN DATA_BACKFILL; board.md:5 OPEN POSTMORTEM_DRAFT.'
json.dump(c,open('/task/workspace/context.json','w'))