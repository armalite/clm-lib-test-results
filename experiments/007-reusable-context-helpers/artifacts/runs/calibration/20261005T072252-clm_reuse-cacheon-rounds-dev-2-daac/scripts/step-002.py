import os,re
from ctx import keep_notes
R='/task/fixtures/round-01'
out=[]
for f in sorted(os.listdir(R+'/logs')):
  for i,l in enumerate(open(R+'/logs/'+f),1):
    if re.search(r'ERROR|WARN|FATAL|CRIT',l) and 'slow query' not in l: out.append(f'{f}:{i} {l.strip()[21:140]}')
print('\n'.join(out[:40]))
keep_notes('R1: changes.md:3 CHG-107 APPLIED retry budget GETs=1. board empty. ctx.py has keep_notes(body) to replace context. Filter: grep ERROR/WARN excluding slow query.\nR1 errors:\n'+'\n'.join(out[:25]))