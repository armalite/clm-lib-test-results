import json,re,glob
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='n1':
        e['body']=e['body'].replace(' Next: advance R10.','')+' R10 board:3 Thread B +payments-svc; :4 Thread C notify-worker request failures cause unknown ongoing; :5 OPEN DATA_BACKFILL; :6 OPEN POSTMORTEM_DRAFT. changes:3 CHG-173 irrelevant.'
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-10/logs/*')):
    for i,l in enumerate(open(f),1):
        if re.search('WARN|ERROR|FATAL',l) and 'slow query' not in l:
            print(f.split('/')[-1],i,l.strip()[:150])