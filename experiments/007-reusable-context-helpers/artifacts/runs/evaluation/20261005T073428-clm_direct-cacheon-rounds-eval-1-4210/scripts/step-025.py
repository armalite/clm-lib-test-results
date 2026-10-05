import json
p='/task/workspace/context.json'
d=json.load(open(p))
n=[e for e in d['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' Next: advance to R8.','')
n+='\nR8: board.md:3 Thread A resolved; :4 Thread B cause revised CERT_EXPIRED; :5 Thread C auth-svc ongoing cause unknown; :6 OPEN ALERT_TUNING. changes.md:3 CHG-157 dashboards. Logs: auth-svc.log:14,16,18,21,22,25,42,46,53,67-69,77 ERROR config validation failed cache.ttl_s=-1 build 4.51.3 (BAD_CONFIG_ROLLOUT, cite r01 changes.md:4). CERT search-api.log:2,22,25,27,28,34,35,37,46,56,62; shipping-svc.log:4,11,19,31,32,38,42,45,75,79. Next: advance to R9.'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open(p,'w'))
print('ok')