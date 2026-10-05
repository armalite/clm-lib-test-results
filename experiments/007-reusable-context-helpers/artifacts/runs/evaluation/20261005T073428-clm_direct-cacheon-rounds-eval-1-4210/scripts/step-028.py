import json
p='/task/workspace/context.json'
d=json.load(open(p))
n=[e for e in d['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance to R9.','')
n+='\nR9: board.md:3 Thread B mitigated; :4 Thread C still restarting; :5 CLOSED POSTMORTEM_DRAFT; :6 OPEN CUSTOMER_COMMS. changes.md:3 CHG-168 log sampling. Logs: auth-svc.log:10,12,22,24,49,51,55,57,58,61,64 config ttl_s=-1; search-api.log:12,36 CERT; shipping-svc.log:53,59 CERT (fewer). Next: advance to R10.'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open(p,'w'))
print('ok')