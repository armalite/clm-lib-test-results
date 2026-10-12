import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
    L=open(f).read().splitlines();hits=[i+1 for i,l in enumerate(L) if re.search(r'429|disk|heap|rss|cache|batch|ERROR|pool|cert|dns|lag',l,re.I)]
    print(f.split('/')[-1],len(hits),hits[:3],hits[-1:] if hits else '')
    if hits: print(' ',L[hits[0]-1][:160])
d=json.load(open('/task/workspace/context.json'))
n=[x for x in d['entries'] if x['id']=='n1'][0]
n['body']+=' R7: board.md:3 Thread A resolved; :4 OPEN DATA_BACKFILL; :5 OPEN POSTMORTEM_DRAFT.'
d['entries']=[n]
json.dump(d,open('/task/workspace/context.json','w'))