open('ctx.py','w').write('''import json
P='/task/workspace/context.json'
def load():
    try: return json.load(open(P))
    except Exception: return {"format":"clm-context/v1","entries":[]}
def save(d): json.dump(d,open(P,'w'))
def keep_notes(note):
    d=load(); d['entries']=[e for e in d['entries'] if e['role']=='note']
    d['entries']=[e for e in d['entries'] if e['id']!='notes']+[{"id":"notes","role":"note","body":note}]
    save(d)
''')
import os
r='/task/fixtures/round-01/'
for f in sorted(os.listdir(r)):print(f)
print(open(r+'board.md').read()[:1500])
for f in os.listdir(r+'logs'):
  L=open(r+'logs/'+f).read().splitlines()
  print(f,len(L))
  for i,l in enumerate(L,1):
    if 'ERROR' in l or 'WARN' in l: print(i,l[:160])