
import os,re,json
R=re.compile(r"heartbeat|health ok|gc cycle|request ok|slow query")
def scan(n):
  b='/task/fixtures/round-%02d/'%n
  for r,d,f in sorted(os.walk(b)):
    for x in sorted(f):
      p=os.path.join(r,x);rel=os.path.relpath(p,'/task/fixtures')
      for i,l in enumerate(open(p).read().splitlines(),1):
        if l.strip() and not R.search(l) and not l.startswith('# '):print(rel+':'+str(i),l[:150])
def setctx(entries):
  json.dump({'format':'clm-context/v1','entries':entries},open('/task/workspace/context.json','w'))
