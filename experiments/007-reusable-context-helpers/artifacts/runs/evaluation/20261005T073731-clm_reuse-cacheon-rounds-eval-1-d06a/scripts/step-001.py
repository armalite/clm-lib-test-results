open('/task/workspace/ctx.py','w').write('''import json
P='/task/workspace/context.json'
def load():
    try: return json.load(open(P))
    except Exception: return {"format":"clm-context/v1","entries":[]}
def save(d): json.dump(d,open(P,'w'))
def keep_notes(note_body):
    d={"format":"clm-context/v1","entries":[{"id":"notes","role":"note","body":note_body}]}
    save(d)
''')
import os,subprocess
r='/task/fixtures/round-01/'
for f in sorted(os.listdir(r))+['logs/'+x for x in sorted(os.listdir(r+'logs'))]:
  if os.path.isfile(r+f):
    L=open(r+f).read().splitlines()
    print('==',f,len(L))
    for i,l in enumerate(L,1):
      if f.endswith('.md') or any(k in l for k in ('ERROR','WARN','error','warn')): print(i,l[:160])
