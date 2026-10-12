import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]['body']
n+=' R4 logs: checkout-api disk used_pct 93-98 /var/data (checkout-api.log:7,17,19,28) - possible DISK_PRESSURE; slow queries noise. No cache-miss lines seen in R4 checkout log (check later). Next: advance to R5.'
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open('/task/workspace/context.json','w'))
print('ok')