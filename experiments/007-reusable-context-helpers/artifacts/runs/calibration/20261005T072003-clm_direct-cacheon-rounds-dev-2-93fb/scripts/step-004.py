import os,json,re
R='/task/fixtures/round-02'
print(open(R+'/board.md').read());print(open(R+'/changes.md').read())
out=[]
for f in sorted(os.listdir(R+'/logs')):
  for i,l in enumerate(open(R+'/logs/'+f),1):
    if not re.search(r'(request ok|gc cycle|health ok|heartbeat)|slow query',l):out.append(f'{f}:{i} {l.strip()[20:140]}')
print(len(out));print('\n'.join(out[:40]))
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; changes.md:3 CHG-107 APPLIED retry budget GETs=1. Logs mostly routine (INFO ok/gc/health/heartbeat, WARN slow query noise). round-01/logs/inventory-svc.log:7,20,50-90 dns SERVFAIL rates.internal. Workflow: per round filter non-routine lines, then advance.'}]}
json.dump(c,open('/task/workspace/context.json','w'))