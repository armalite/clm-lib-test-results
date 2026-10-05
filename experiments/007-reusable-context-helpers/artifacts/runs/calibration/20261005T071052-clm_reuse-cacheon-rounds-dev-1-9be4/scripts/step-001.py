open('ctx.py','w').write('''import json
P='/task/workspace/context.json'
def load():
    try: return json.load(open(P))
    except Exception: return {"format":"clm-context/v1","entries":[]}
def save(d): json.dump(d,open(P,'w'))
def keep_notes(note_id, body):
    d=load(); d['entries']=[e for e in d['entries'] if e['role']=='note' and e['id']!=note_id]
    d['entries'].append({'id':note_id,'role':'note','body':body}); save(d)
''')
import os
for r,_,f in os.walk('/task/fixtures/round-01'):
  for x in f:
    p=os.path.join(r,x);L=open(p).read().splitlines();print(p,len(L))
    for i,l in enumerate(L[:12],1):print(i,l[:150])