import json
h='''import os,re
def scan(n):
  b='/task/fixtures/round-%02d'%n
  for r,d,f in os.walk(b):
    for x in sorted(f):
      p=os.path.join(r,x);rel=os.path.relpath(p,'/task/fixtures')
      for i,l in enumerate(open(p),1):
        if x.endswith('.md'):
          if l.strip() and not l.startswith('#'):print(rel,i,l.rstrip()[:150])
        elif 'slow query' not in l and re.search(r'ERROR|WARN|error|warn|FATAL|level=(e|w)',l):print(rel,i,l.rstrip()[:130])
'''
open('/task/workspace/h.py','w').write(h)
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'R1: board empty. changes.md:3 CHG-107 APPLIED retry budget GETs=1. slow query WARNs in all services = background noise. inventory-svc DNS SERVFAIL host=rates.internal lines 7,20,50,54,57,62,65,85,86,89,90 (round-01/logs/inventory-svc.log). Helper: from h import scan; scan(n) prints non-noise lines.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
import h;h.scan(1)