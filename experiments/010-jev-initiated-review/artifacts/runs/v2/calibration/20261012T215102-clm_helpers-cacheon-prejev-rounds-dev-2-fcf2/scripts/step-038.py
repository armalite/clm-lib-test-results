import json
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+="\nR9: raw grep output in /task/workspace/spill/s36.obs.txt (not yet summarized; read it next, print compactly)."
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
s=open('/task/workspace/spill/s36.obs.txt').read()
import re
for l in s.splitlines():
  if l.startswith(('board','changes')):print(l[:200])
  else:
    m=re.match(r'(\S+) (\d+) ',l)
    if m:print(m.group(1),m.group(2),re.sub(r'^.*?(level|msg)','',l)[:90])