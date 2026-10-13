import json
n=open('/task/workspace/context.json').read()
c=json.load(open('/task/workspace/context.json'))
b=c['entries'][0]['body']+"\nR3: board.md:3 Thread A UPSTREAM_RATE_LIMIT pricing-svc+search-api ongoing. pricing-svc.log:4-64 429 sms-gateway; search-api.log:8-79 429 sms-gateway. checkout/inventory/shipping clean."
c={'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':b}]}
json.dump(c,open('/task/workspace/context.json','w'))