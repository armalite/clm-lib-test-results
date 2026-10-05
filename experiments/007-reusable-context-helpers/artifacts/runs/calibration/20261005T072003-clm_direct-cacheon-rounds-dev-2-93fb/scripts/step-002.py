import os,json,re
R='/task/fixtures/round-01'
out=[]
for f in sorted(os.listdir(R+'/logs')):
  for i,l in enumerate(open(R+'/logs/'+f),1):
    if not re.search(r'INFO .*(request ok|gc cycle|health ok|heartbeat)|slow query',l):out.append(f'{f}:{i} {l.strip()[20:150]}')
print('\n'.join(out[:60]))
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; changes.md:3 CHG-107 APPLIED retry budget GETs=1. Logs mostly routine (INFO ok/gc/health/heartbeat, WARN slow query noise). inventory-svc.log:7 dns SERVFAIL rates.internal. Workflow: per round filter non-routine lines, then advance.'}]}
json.dump(c,open('/task/workspace/context.json','w'))