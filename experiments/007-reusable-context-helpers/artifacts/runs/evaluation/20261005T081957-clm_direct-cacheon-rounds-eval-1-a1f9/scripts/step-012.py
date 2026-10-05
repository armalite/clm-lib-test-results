import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3')]
e.append({'id':'n4','role':'note','body':'R4: board.md:3 Thread B shipping-svc DB_POOL_EXHAUSTED ongoing (board guess; logs disagree). board.md:4 follow-up OPEN RUNBOOK_UPDATE. changes CHG-133 dashboards (noise). shipping-svc.log ERRORs tls handshake failed peer=sso.example.net certificate_expired lines 1-85 (e.g. 1,2,4,13,85) -> real cause CERT_EXPIRED. No DB pool errors seen. Lag WARNs payments(27-72) ledger(28-77) still fluctuating 22k-80k. Next: advance to R5.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))