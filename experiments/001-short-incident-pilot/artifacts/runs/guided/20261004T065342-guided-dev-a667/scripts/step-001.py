import os
os.makedirs('helpers',exist_ok=True)
open('helpers/__init__.py','w').write('')
open('helpers/ctx.py','w').write('''import json
P='/task/workspace/context.json'
def load():
    try: return json.load(open(P))
    except Exception: return {"format":"clm-context/v1","entries":[]}
def compact(note, keep_last=0):
    d=load(); e=d['entries']
    kept=e[-keep_last:] if keep_last else []
    d['entries']=[{"id":"notes","role":"note","body":note}]+[x for x in kept if x['id']!='notes']
    json.dump(d,open(P,'w'))
''')
for f in ['config/shipping-api.yaml','deploy/changes.log','ops/oncall-notes.md']:
    print('==',f)
    for i,l in enumerate(open('/task/fixtures/'+f),1): print(i,l.rstrip())