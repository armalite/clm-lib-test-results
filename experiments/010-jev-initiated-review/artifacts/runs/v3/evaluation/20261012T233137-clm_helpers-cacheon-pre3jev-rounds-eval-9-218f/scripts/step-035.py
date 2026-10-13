import json
c=json.load(open('/task/workspace/context.json'))
keep=[e for e in c['entries'] if e['id'] in ('n1','n2','n3','n4','n5','n6','n7','n8')]
json.dump({'format':'clm-context/v1','entries':keep},open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-09/board.md').read()[:800])
import re
for i,x in enumerate(open('/task/fixtures/round-09/logs/search-api.log'),1):
  if re.search('config|ERROR',x): print(i,x[:110].rstrip());break