import re
b='/task/fixtures/stage-2/'
L=open(b+'logs/quotes-api.log').readlines()
n=0
for i,l in enumerate(L):
  if ('ERROR' in l or 'WARN' in l) and 'risk-score' not in l and l[11:16]>='09:35':
    n+=1
    if n<4:print(i+1,l.strip()[:170])
print(n)
G=open(b+'logs/api-gateway.log').readlines()
print([i+1 for i,l in enumerate(G) if '5xx' in l or ' 503' in l][:5])
open('/task/workspace/notes.txt','a').write('s2 CHG-5117 APPLIED changes.log:1 timeout 3500 09:35; post errors dbpool?\n')