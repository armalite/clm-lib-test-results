import sys;sys.path.insert(0,'/task/workspace')
import regmaint
c=regmaint.load();c['entries']=[e for e in c['entries'] if not e['id'].startswith(('s9.','s10.','s11.','s12.'))]
for e in c['entries']:
  if e['id']=='n1':e['body']='Stages1-4 done: exporter/core.py implements S1-S4 (JSON+exported_by; owner scope S4.2; regulator purpose S4.1 adds confidential_count per S2.5). Helper /task/workspace/regmaint.py: regmaint.update(N) per stage; override(eid,body,reason).'
regmaint.save(c);print('ok')