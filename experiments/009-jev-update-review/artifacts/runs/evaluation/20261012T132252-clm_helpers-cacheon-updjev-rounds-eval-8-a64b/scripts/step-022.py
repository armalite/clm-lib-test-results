import json,re,glob
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if not e['id'].startswith(('s20','s21'))]
for e in c['entries']:
    if e['id']=='n3': e['body']+=' [HIST: B cause revised R8]'
    if e['id']=='n6': e['body']=e['body'].replace('Next: advance to R7.','').replace('D DNS_RESOLUTION notify-worker ongoing','D DNS (later false alarm R8)')
c['entries'].append({'id':'n8','role':'note','body':'R8 board: A MEMORY_LEAK resolved (round-08/board.md:3); B revised DB_POOL_EXHAUSTED inventory-svc (round-08/board.md:4); D false alarm closed (round-08/board.md:5). CHG-113 notify-worker pool_max=-4 still unseen in errors.'})
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search('ERROR|WARN|error|warn',l): print(f.split('/')[-1],i,l.strip()[:110])