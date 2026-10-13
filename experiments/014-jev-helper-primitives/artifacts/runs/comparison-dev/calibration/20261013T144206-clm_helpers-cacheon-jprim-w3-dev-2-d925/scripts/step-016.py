import sys,subprocess,re
sys.path.insert(0,'/task/workspace')
import regtool
p='/task/workspace/exporter/core.py'
s=open(p).read()
for i,l in enumerate(s.split('\n')):
    if 'eu' in l or 'region' in l: print(i,l)
c=regtool.load()
reg=[e for e in c['entries'] if e['id']=='register'][0]['body']
lines=reg.split('\n')
items={str(k):l for k,l in enumerate(lines) if l.startswith('CURRENT')}
aff=regtool.affected({'S6.1':'Residency restriction withdrawn: records of every region exported under ordinary rules.'},items);print({n:{k:v for k,v in d.items() if (v or 0)>0.5} for n,d in aff.items()})
out=[]
for l in lines:
    if l.startswith('CURRENT [S2.6]'):
        out.append("HISTORY [S2.6, S6.1] Region 'eu' restriction (needed 'eu' in user regions) withdrawn by S6.1; all regions exported under ordinary rules.")
    else: out.append(l)
out.append('HISTORY [S6.2] Note: web UI shows 50 records/page; exports unchanged.')
regtool.set_entry(c,'register','\n'.join(out))
regtool.set_entry(c,'note1','Stages 1-5 in core.py; S6 eu filter removal in progress. Helper regtool.py.','note')
c['entries']=[e for e in c['entries'] if e['id'] in('register','note1')]
regtool.save(c)