import json,re,glob
b='/task/fixtures/round-10/'
for f in ['board.md','changes.md']:
    for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for f in sorted(glob.glob(b+'logs/*.log')):
    hits=[i for i,l in enumerate(open(f),1) if re.search('429|ttl_s|pool|exhaust|ERROR',l)]
    print(f.split('/')[-1],len(hits),hits[:15])
n=json.load(open('/task/workspace/context.json'))['entries'][:9]
json.dump({'format':'clm-context/v1','entries':n},open('/task/workspace/context.json','w'))