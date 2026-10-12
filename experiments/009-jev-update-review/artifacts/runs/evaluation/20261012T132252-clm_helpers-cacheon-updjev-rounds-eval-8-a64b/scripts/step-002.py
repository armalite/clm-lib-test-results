import os,re
b='/task/fixtures/round-01/logs/'
for f in sorted(os.listdir(b)):
  for i,l in enumerate(open(b+f)):
    if ('ERR' in l or 'WARN' in l) and 'slow query' not in l:print(f,i+1,l.strip()[:140])