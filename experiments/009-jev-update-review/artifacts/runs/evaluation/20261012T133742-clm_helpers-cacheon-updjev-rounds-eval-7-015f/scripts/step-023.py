import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
    for i,l in enumerate(open(f),1):
        if re.search(r'429|used_pct|cache|pool|cert|dns|error',l,re.I) and not re.search('slow',l,re.I):
            print(f.split('/')[-1],i,l.strip()[:110])
d=json.load(open('/task/workspace/context.json'))
d['entries']=[e for e in d['entries'] if e['id']=='n1']
d['entries'][0]['body']=d['entries'][0]['body'].replace("r7: board empty; no 429s; checkout disk 92-98 lines 13,19,46; payments-svc disk 91-98 lines 3,27,62 (DISK_PRESSURE spreading to payments-svc). Round 7 done; next: advance. ",'',1)+' R8: board.md:3 Thread B now also payments-svc (cause/status unchanged); board.md:4 OPEN RUNBOOK_UPDATE.'
json.dump(d,open('/task/workspace/context.json','w'))