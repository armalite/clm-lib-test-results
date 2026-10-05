open('ctx.py','w').write('''import json
P='/task/workspace/context.json'
def load():
    try: return json.load(open(P))
    except Exception: return {"format":"clm-context/v1","entries":[]}
def save(d): json.dump(d,open(P,'w'))
def keep_notes(note_id, body):
    d=load(); e=[x for x in d['entries'] if x['role']=='note' and x['id']!=note_id]
    e.append({'id':note_id,'role':'note','body':body}); d['entries']=e; save(d)
''')
import os,subprocess
r='/task/fixtures/round-01/'
for f in sorted(os.listdir(r)):print(f)
print(open(r+'board.md').read()[:1500])
if os.path.exists(r+'changes.md'):print(open(r+'changes.md').read()[:1000])
for f in sorted(os.listdir(r+'logs')):
  L=open(r+'logs/'+f).read().splitlines()
  print(f,len(L));[print(i+1,l[:160]) for i,l in enumerate(L) if any(k in l for k in ('ERROR','WARN','error'))][:0]
  bad=[(i+1,l[:150]) for i,l in enumerate(L) if 'ERROR' in l or 'WARN' in l]
  for b in bad[:4]:print(*b)