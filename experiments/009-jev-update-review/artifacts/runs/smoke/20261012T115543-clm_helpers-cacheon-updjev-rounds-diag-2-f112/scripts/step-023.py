import json,re
L=open('/task/fixtures/round-07/logs/notify-worker.log').read().splitlines()
for i,l in enumerate(L,1):
  if re.search(r'ERROR|WARN|pool|fail',l,re.I): print(i,l[:150])
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='notes'][0]
n['body']+=' R7 board: Thread A CERT resolved round-07/board.md:3; Thread B revised DISK_PRESSURE board.md:4; Thread C notify-worker failures ongoing board.md:5 (likely CHG-113 pool_max=0).'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))