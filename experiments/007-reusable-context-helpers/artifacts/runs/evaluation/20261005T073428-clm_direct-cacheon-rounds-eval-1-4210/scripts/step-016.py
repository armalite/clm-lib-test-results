import json
p='/task/workspace/context.json'
d=json.load(open(p))
n=[e for e in d['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance to R5.','')
n+='\nR5: board.md:3 Thread A mitigated (after CHG-143). changes.md:3 CHG-143 APPLIED mitigation thread A payments-svc. Logs: no lag lines matched in payments/ledger. CERT_EXPIRED sso.example.net now also search-api.log:14,35,50,51,79,81; shipping-svc.log:1,2,18,27,56,59 still. Next: advance to R6.'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open(p,'w'))
print('ok')