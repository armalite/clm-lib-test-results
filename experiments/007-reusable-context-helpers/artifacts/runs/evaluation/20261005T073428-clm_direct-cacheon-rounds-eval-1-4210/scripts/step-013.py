import json
p='/task/workspace/context.json'
d=json.load(open(p))
n=[e for e in d['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance to R4.','')
n+='\nR4: board.md:3 Thread B shipping-svc DB_POOL_EXHAUSTED ongoing (board likely wrong); board.md:4 follow-up OPEN RUNBOOK_UPDATE. changes.md:3 CHG-133 dashboards. Logs: shipping-svc.log:1-24,40-85 ERROR tls handshake peer=sso.example.net certificate_expired (real cause CERT_EXPIRED). No pool errors seen. Next: advance to R5.'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open(p,'w'))
print('ok')