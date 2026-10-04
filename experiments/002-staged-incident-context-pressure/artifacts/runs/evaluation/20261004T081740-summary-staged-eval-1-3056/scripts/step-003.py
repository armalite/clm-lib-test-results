import re
L=open('/task/fixtures/stage-1/logs/quotes-api.log').readlines()
for i,l in enumerate(L):
  if 'db pool' in l: print(i+1,l.strip()[:160])
G=open('/task/fixtures/stage-1/logs/api-gateway.log').readlines()
n=[i+1 for i,l in enumerate(G) if re.search(r'status=5\d\d',l)]
print(len(n),n[:5]);print(G[n[0]-1].strip()[:200] if n else '')
open('/task/workspace/notes.txt','w').write('s1: RN line9 risk timeout 800 (from 2500); RN line15 pool 14. qlog 206 first risk timeout ERROR\n')