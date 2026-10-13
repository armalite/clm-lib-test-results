import json
n=open('/task/workspace/context.json').read()
d=json.loads(n)
b=d['entries'][0]['body']
b=b.replace('\nTool:','\nR4: board empty update. auth-svc.log:3-57 dns errs; checkout-api.log:2-64 dns errs; search-api.log:4-90 429 fx-rates. No changes.\nTool:')
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':b}]},open('/task/workspace/context.json','w'))