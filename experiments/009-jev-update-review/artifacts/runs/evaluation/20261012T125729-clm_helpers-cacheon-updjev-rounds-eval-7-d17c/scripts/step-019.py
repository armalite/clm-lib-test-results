import json
n=json.load(open('/task/workspace/context.json'))['entries'][0]['body']
n+=' R7 logs: disk usage high WARNs checkout-api lines 13,17,19.. and payments-svc lines 3,4,9.. (watch DISK_PRESSURE; board silent); ledger/search/shipping clean. NEXT: advance to R8.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))
print('ok')