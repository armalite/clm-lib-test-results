import json
c=json.load(open('/task/workspace/context.json'))
n1=[e for e in c['entries'] if e['id']=='n1'][0]
b=n1['body']
i=b.find('R6 raw:')
b=b[:i]+'R6: board.md:3 Thread A mitigated; board.md:4 OPEN ALERT_TUNING; changes.md:3 CHG-150 APPLIED mitigation search-api. 429 tax-provider checkout-api.log:21-74, ledger-svc.log:17-76.\nR7: board.md:3 Thread B adds checkout-api, cause/status unchanged; changes.md:3 CHG-152 PROPOSED ignore. 429 checkout-api.log:4-49, ledger-svc.log:13-77.\nNext: advance to round 8.'
n1['body']=b
json.dump({'format':'clm-context/v1','entries':[n1]},open('/task/workspace/context.json','w'))
print('ok')