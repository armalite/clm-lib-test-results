import re
b='/task/fixtures/stage-1/logs/'
L=open(b+'returns-svc.log').readlines()
n=sum('timed out' in l for l in L);print('timeouts',n)
for i,l in enumerate(L,1):
 if 'tax-engine' in l and 'ERROR' not in l:print(i,l.strip());break
E=open(b+'edge-gw.log').readlines()
for i,l in enumerate(E,1):
 if ' 5' in l and 'returns' in l:print(i,l.strip());break