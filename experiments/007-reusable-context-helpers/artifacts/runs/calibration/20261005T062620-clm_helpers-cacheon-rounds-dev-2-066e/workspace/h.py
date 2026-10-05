import os,re
def scan(n):
  b='/task/fixtures/round-%02d'%n
  for r,d,f in os.walk(b):
    for x in sorted(f):
      p=os.path.join(r,x);rel=os.path.relpath(p,'/task/fixtures')
      for i,l in enumerate(open(p),1):
        if x.endswith('.md'):
          if l.strip() and not l.startswith('#'):print(rel,i,l.rstrip()[:150])
        elif 'slow query' not in l and re.search(r'ERROR|WARN|error|warn|FATAL|level=(e|w)',l):print(rel,i,l.rstrip()[:130])
