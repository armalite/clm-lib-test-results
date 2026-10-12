import json,re
c=json.load(open('/task/workspace/context.json'))
s=c['entries'][0]['body'].replace('R9 board not yet reviewed in notes. Next: advance to R10.','R9 board empty. R10: Thread C opened checkout-api request failures cause unknown, ongoing (round-10/board.md:3); CHG-173 PROPOSED only (round-10/changes.md:3).')
c['entries']=[{'id':'sum1','role':'summary','body':s}]
json.dump(c,open('/task/workspace/context.json','w'))
from collections import Counter
L=open('/task/fixtures/round-10/logs/checkout-api.log').read().splitlines()
k=Counter()
for i,l in enumerate(L,1):
  if re.search('ERROR|WARN|error|fail',l):
    m=re.sub(r'[0-9:.TZ-]{8,}','',l)[:90];k[m[:60]]+=1
    if k[m[:60]]<=2: print(i,l[:200])