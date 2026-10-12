import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
    L=open(f).read().splitlines()
    hits=[(i+1,l[:110]) for i,l in enumerate(L) if re.search(r'429|pool|miss|disk|cert|dns|lag|memory|OOM',l,re.I)]
    print(f.split('/')[-1],len(hits),hits[:4])
print(open('/task/fixtures/round-05/board.md').read())
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance to R5.','')+' R5: CHG-137 PROPOSED HPA search (not applied, r5 changes.md:3).'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open('/task/workspace/context.json','w'))