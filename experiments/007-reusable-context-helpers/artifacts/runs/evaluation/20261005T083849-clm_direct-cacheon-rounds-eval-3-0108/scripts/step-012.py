import re,os,json
b='/task/fixtures/round-04/logs/'
for f in sorted(os.listdir(b)):
  for i,l in enumerate(open(b+f),1):
    if re.search(r'429|disk|space|cert|inflight|WARN|fail',l,re.I) and 'slow query' not in l:print(f,i,l.rstrip()[:140])
notes=open('/task/workspace/notes.txt').read()+'\nR4: board A mitigated (round-04/board.md:3); B checkout-api UPSTREAM_RATE_LIMIT ongoing (:4); D search-api DISK_PRESSURE ongoing (:5); FU OPEN CUSTOMER_COMMS,POSTMORTEM_DRAFT,CAPACITY_REVIEW (:6-8). CHG-136 APPLIED ledger mitigation A (round-04/changes.md:4); CHG-133 retry.'
open('/task/workspace/notes.txt','w').write(notes)
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':notes}]},open('/task/workspace/context.json','w'))