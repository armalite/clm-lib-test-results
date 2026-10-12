import json,re
b='/task/fixtures/round-05/logs/'
import os
for f in sorted(os.listdir(b)):
  L=open(b+f).read().splitlines()
  hits=[(i+1,l[:110]) for i,l in enumerate(L) if re.search(r'ERROR|SERVFAIL|certificate|429|pool|max_inflight|OOM|disk',l,re.I)]
  print(f,len(hits),[h[0] for h in hits][:15]);
  for h in hits[:2]:print(' ',h)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]
c['entries'][3]['body']=c['entries'][3]['body'].replace(' Next: advance to R5.','')
c['entries'].append({'id':'n5','role':'note','body':'R5: board.md:3 Thread A (DNS) mitigated; changes.md:3 CHG-143 APPLIED inventory-svc mitigation. board.md:4 Thread B adds shipping-svc (board cause still DB_POOL, logs say CERT_EXPIRED). Follow-ups OPEN: VENDOR_TICKET board.md:5, ALERT_TUNING board.md:6.'})
json.dump(c,open('/task/workspace/context.json','w'))