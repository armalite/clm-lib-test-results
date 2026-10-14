import sys;sys.path.insert(0,'/task/workspace')
print(open('/task/workspace/exporter/core.py').read())
import regmaint
c=regmaint.load();c['entries']=[e for e in c['entries'] if not e['id'].startswith(('s17.','s18.','s19.','s20.'))]
for e in c['entries']:
  if e['id']=='n1':e['body']='Stages1-6 done: core.py implements S1-S6 (residency removed). Helper regmaint.py: regmaint.update(N) per stage; override(eid,body,reason).'
regmaint.save(c)