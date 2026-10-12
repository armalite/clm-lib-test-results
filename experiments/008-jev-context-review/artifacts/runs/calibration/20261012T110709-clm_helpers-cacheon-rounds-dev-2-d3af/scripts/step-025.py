import json
L=open('/task/fixtures/round-08/logs/search-api.log').read().splitlines()
ln=[i+1 for i,l in enumerate(L) if 'config validation failed' in l]
l4=[i+1 for i,l in enumerate(L) if '429' in l and 'ERROR' in l]
print(ln,l4)
for i in ln[:1]:print(L[i-1][:300])
p='/task/workspace/context.json'
n=json.load(open(p))['entries'][0]['body']
n+=' R8 search-api errs: config validation failed x9 lines %s (BAD_CONFIG likely CHG-120), 429 x6 lines %s.'%(ln,l4)
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open(p,'w'))