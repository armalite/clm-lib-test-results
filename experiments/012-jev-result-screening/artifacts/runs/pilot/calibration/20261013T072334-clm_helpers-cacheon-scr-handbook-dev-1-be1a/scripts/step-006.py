import json
t=open('/task/workspace/spill/s5.obs.txt').read()
import re
for l in t.split('\n'):
    if re.search(r'§|##|\d',l): print(l[:170])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
json.dump(c,open('/task/workspace/context.json','w'))