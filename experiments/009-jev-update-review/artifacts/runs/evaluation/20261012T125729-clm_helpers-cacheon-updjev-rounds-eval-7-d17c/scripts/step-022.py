import json
c=json.load(open('/task/workspace/context.json'))
n=c['entries'][0]['body']+' R8 logs (JSON format): disk usage high checkout-api lines 1,5,19,23..; payments-svc lines 2,7,9..; ledger slow query only. NEXT: advance to R9.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))