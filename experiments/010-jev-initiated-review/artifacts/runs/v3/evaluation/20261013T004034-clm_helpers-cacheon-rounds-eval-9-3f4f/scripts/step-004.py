import os,json,re
r='/task/fixtures/round-02/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(r+f),1):print(f,i,l.rstrip())
b=r+'logs/'
out=[]
for f in sorted(os.listdir(b)):
  for i,l in enumerate(open(b+f),1):
    if not re.search(r'heartbeat|health ok|request ok|gc cycle|slow query',l):out.append(f'{f}:{i} {l.strip()[:140]}')
print(len(out));print('\n'.join(out[:35]))
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty; changes.md:3 CHG-108 APPLIED TLS session ticket rotation hourly. Logs routine lines: heartbeat/health/request ok/gc/slow query. services: notify-worker shipping-svc ledger-svc inventory-svc search-api. Round 2 released (step3).'}]},open('/task/workspace/context.json','w'))