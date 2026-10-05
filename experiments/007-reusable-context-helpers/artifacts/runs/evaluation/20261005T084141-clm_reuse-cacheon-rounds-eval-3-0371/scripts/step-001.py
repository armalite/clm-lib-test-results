open('ctx.py','w').write('''import json
P='/task/workspace/context.json'
def load():
    try: return json.load(open(P))
    except Exception: return {"format":"clm-context/v1","entries":[]}
def save(d): json.dump(d,open(P,'w'))
def reset(notes):
    save({"format":"clm-context/v1","entries":[{"id":"n%d"%i,"role":"note","body":b} for i,b in enumerate(notes)]})
''')
import os,subprocess
r='/task/fixtures/round-01/'
for f in sorted(os.listdir(r)):print(f)
print(open(r+'board.md').read()[:1500])
for f in sorted(os.listdir(r+'logs')):
  L=open(r+'logs/'+f).read().splitlines()
  print(f,len(L));[print(i+1,l[:150]) for i,l in enumerate(L) if 'ERROR' in l or 'WARN' in l][:6]