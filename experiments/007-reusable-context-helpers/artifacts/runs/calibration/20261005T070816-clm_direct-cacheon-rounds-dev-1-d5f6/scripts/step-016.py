import json
p='/task/workspace/context.json'
c=json.load(open(p))
e=[x for x in c['entries'] if x['id'] in('n1','n2','n3','n4')]
e.append({'id':'n5','role':'note','body':'R5: Thread A mitigated (round-05/board.md:3) via CHG-143 auth-svc (round-05/changes.md:4); no db pool errors in R5 logs. Thread B adds checkout-api (round-05/board.md:4); 429 fx-rates still: round-05/logs/checkout-api.log:21, payments-svc.log:13. Follow-up OPEN CAPACITY_REVIEW (round-05/board.md:5). CHG-138 APPLIED TLS rotation hourly (round-05/changes.md:3). Next: advance to R6.'})
json.dump({'format':'clm-context/v1','entries':e},open(p,'w'))
print('ok')