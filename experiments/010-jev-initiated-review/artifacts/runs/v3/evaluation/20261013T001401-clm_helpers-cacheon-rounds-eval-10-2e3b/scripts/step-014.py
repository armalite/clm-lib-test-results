import json
d=json.load(open('/task/workspace/context.json'))
b=d['entries'][0]['body']
b=b.replace('\nTool:','\nR5: board empty. changes:3 CHG-140 log sampling irrelevant. auth-svc.log:1-60 dns; checkout-api.log:2-66 dns; search-api.log:5-64 429 fx-rates.\nTool:')
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':b}]},open('/task/workspace/context.json','w'))