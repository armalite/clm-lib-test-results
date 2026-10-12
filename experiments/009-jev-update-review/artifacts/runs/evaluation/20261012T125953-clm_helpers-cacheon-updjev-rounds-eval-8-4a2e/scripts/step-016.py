import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'WARN|ERROR|dns|DNS|pool|heap|restart|OOM',l):
            print(f.split('/')[-1],i,l.strip()[:110])
c=json.load(open('/task/workspace/context.json'))
n1=[e for e in c['entries'] if e['id']=='n1'][0]
n1['body']=n1['body'].replace(' Next: advance to r6.','')+' R6: board.md:3 Thread A mitigated; board.md:4 Thread D DNS_RESOLUTION notify-worker ongoing; changes.md:4 CHG-150 APPLIED mitigation pricing-svc (only pricing; auth?); CHG-147 minor.'
c['entries']=[n1]
json.dump(c,open('/task/workspace/context.json','w'))