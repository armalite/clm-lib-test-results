import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
    L=open(f).read().splitlines()
    hits=[i+1 for i,l in enumerate(L) if re.search(r'429|ERROR|cache|batch|pool|cert|dns|disk|memory|lag',l,re.I)]
    print(f.split('/')[-1],len(hits),hits[:3],hits[-1:] , L[hits[0]-1][:160] if hits else '')
d=json.load(open('/task/workspace/context.json'))
n=[x for x in d['entries'] if x['id']=='n1'][0]
n['body']+=' R4: board.md:3 Thread A mitigated; board.md:4 OPEN RUNBOOK_UPDATE; changes.md:3 CHG-128 APPLIED retry GETs=1; changes.md:4 CHG-136 APPLIED mitigation A ledger-svc.'
d['entries']=[n]
json.dump(d,open('/task/workspace/context.json','w'))