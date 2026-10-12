import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|429|FATAL|stampede|batch_size',l): print(f.split('/')[-1],i,l.strip()[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
c['entries'].append({'id':'n4','role':'note','body':'R4: board round-04/board.md:3 Thread A mitigated; :4 follow-up OPEN RUNBOOK_UPDATE. changes round-04/changes.md:3 CHG-128 retry GETs=1; :4 CHG-136 APPLIED mitigation thread A ledger-svc.'})
json.dump(c,open('/task/workspace/context.json','w'))