import re,json
b='/task/fixtures/round-06/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['auth-svc','checkout-api','search-api','inventory-svc','shipping-svc']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  e=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('ERROR|WARN|error|429|dns',l)]
  print(s,len(e),e[:2],e[-1:] if e else '')
n=open('notes.md').read()
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('context.json','w'))