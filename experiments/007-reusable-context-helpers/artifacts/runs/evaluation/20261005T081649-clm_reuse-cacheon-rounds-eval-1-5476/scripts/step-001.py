open('ctx.py','w').write('''import json
P='/task/workspace/context.json'
def load():
    try: return json.load(open(P))
    except Exception: return {"format":"clm-context/v1","entries":[]}
def save(d): json.dump(d,open(P,'w'))
def setnote(i,b):
    d=load(); d['entries']=[e for e in d['entries'] if e['id']!=i]; d['entries'].insert(0,{'id':i,'role':'note','body':b}); save(d)
def prune(keep=('notes',)):
    d=load(); d['entries']=[e for e in d['entries'] if e['id'] in keep]; save(d)
''')
import os
r='/task/fixtures/round-01/'
for f in sorted(os.listdir(r)): print(f)
print(open(r+'board.md').read()[:1500])
for f in sorted(os.listdir(r+'logs')):
  L=open(r+'logs/'+f).read().splitlines()
  print(f,len(L))
  for i,l in enumerate(L,1):
    if any(k in l for k in ('ERROR','WARN','error','warn')): print(i,l[:160])
