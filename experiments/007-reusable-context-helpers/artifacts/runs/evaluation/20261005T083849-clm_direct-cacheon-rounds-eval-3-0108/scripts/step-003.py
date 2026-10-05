import json,re,glob
notes='R1: CHG-113 APPLIED search-api 4.16.4 sets http.max_inflight=-1 (round-01/changes.md:4); CHG-114 checkout no cfg; CHG-109 PROPOSED. ledger-svc CERT_EXPIRED sso.example.net round-01/logs/ledger-svc.log:14-21 (ERRORs thru :72). board r1 empty. slow query WARNs everywhere = noise.'
open('/task/workspace/notes.txt','w').write(notes)
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':notes}]},open('/task/workspace/context.json','w'))
for p in sorted(glob.glob('/task/fixtures/round-01/logs/*.log')):
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|WARN',l) and 'slow query' not in l and 'certificate_expired' not in l: print(p.split('/')[-1],i,l.strip()[:150])