import json
print(open('/task/fixtures/round-02/board.md').read());print(open('/task/fixtures/round-02/changes.md').read())
s=open('/task/workspace/spill/s5.obs.txt').read()
import re
from collections import Counter
ls=[l for l in s.splitlines() if l.strip()]
print(len(ls))
for l in ls[:40]: print(l[:150])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))