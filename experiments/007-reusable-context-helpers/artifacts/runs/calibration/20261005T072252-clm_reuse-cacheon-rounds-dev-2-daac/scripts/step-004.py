import os,re
from ctx import keep_notes
R='/task/fixtures/round-02'
print(open(R+'/board.md').read());print(open(R+'/changes.md').read())
out=[]
for f in sorted(os.listdir(R+'/logs')):
  c={}
  for i,l in enumerate(open(R+'/logs/'+f),1):
    if re.search(r'ERROR|WARN|FATAL|CRIT|error|warn',l) and 'slow query' not in l:
      k=re.sub(r'\d+','#',l[21:120]);c.setdefault(k,[]).append(i)
  for k,v in c.items(): out.append(f'{f}:{v[0]}-{v[-1]} n={len(v)} {k.strip()}')
print('\n'.join(out[:30]))
keep_notes('R1: changes.md:3 CHG-107 APPLIED retry budget GETs=1. board empty. ctx.py keep_notes(body). R1 errs: inventory-svc.log:7-90 n=11 dns lookup failed host=rates.internal SERVFAIL.\nR2 (see stdout of step4, re-summarize next step):\n'+'\n'.join(out[:20]))