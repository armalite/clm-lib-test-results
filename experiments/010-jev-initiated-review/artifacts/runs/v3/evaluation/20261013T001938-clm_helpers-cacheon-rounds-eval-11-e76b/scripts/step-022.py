import json,re
R='/task/fixtures/round-08/'
print(open(R+'board.md').read());print(open(R+'changes.md').read())
import os
for f in sorted(os.listdir(R+'logs')):
    h=[(i,l) for i,l in enumerate(open(R+'logs/'+f),1) if re.search(r'ERROR|FATAL|CRIT|429|exhaust|expired|NXDOMAIN|SERVFAIL|lag|OOM|disk|batch|heap|restart',l,re.I)]
    print(f,len(h),h[0][0] if h else '',h[-1][0] if h else '',h[0][1][:160] if h else '')
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
json.dump(c,open('/task/workspace/context.json','w'))