import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
    L=open(f).read().splitlines();hits=[i+1 for i,l in enumerate(L) if re.search(r'ERROR|429|disk|cache|mem|batch',l,re.I) and 'slow query' not in l]
    print(f.split('/')[-1],len(hits),hits[:1],hits[-1:] if hits else '', (L[hits[0]-1][:150] if hits else ''))
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']+=' R5: board.md:3 VENDOR_TICKET open.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))