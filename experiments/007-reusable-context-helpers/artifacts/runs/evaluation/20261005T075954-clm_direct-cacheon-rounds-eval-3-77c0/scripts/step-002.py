import json,os
b='/task/fixtures/round-01/'
out=[]
for x in sorted(os.listdir(b+'logs')):
  for i,l in enumerate(open(b+'logs/'+x)):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l and 'certificate_expired' not in l:out.append(f'{x}:{i+1} {l.strip()[:120]}')
print('\n'.join(out[:40]))
n='R1: board empty. changes.md:3 CHG-113 APPLIED search-api http.max_inflight=-1 (suspect BAD_CONFIG); CHG-114 checkout no cfg; CHG-109 PROPOSED. slow query WARNs everywhere = noise. ledger-svc.log:14,15,21,39,40 CERT_EXPIRED peer=sso.example.net.'
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]}
json.dump(c,open('/task/workspace/context.json','w'))