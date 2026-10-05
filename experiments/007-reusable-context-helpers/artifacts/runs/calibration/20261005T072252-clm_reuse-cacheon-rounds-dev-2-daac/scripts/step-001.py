open('ctx.py','w').write('''import json
P='/task/workspace/context.json'
def load():
    try: return json.load(open(P))
    except Exception: return {"format":"clm-context/v1","entries":[]}
def save(d): json.dump(d,open(P,'w'))
def keep_notes(note_body):
    d={"format":"clm-context/v1","entries":[{"id":"notes","role":"note","body":note_body}]}
    save(d)
''')
import os
for r,ds,fs in os.walk('/task/fixtures/round-01'):
  for f in fs:
    p=os.path.join(r,f);L=open(p).read().splitlines();print('==',p,len(L))
    for i,l in enumerate(L[:12],1):print(i,l[:150])