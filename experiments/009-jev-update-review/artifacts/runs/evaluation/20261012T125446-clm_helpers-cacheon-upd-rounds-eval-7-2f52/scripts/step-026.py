import json,re,glob
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  hits=[(i,l.strip()[:150]) for i,l in enumerate(open(f),1) if re.search('ERROR|WARN|429|disk|pool',l) and 'slow query' not in l]
  print(f.split('/')[-1],len(hits))
  for h in hits[:4]: print(' ',h)
c=json.load(open('/task/workspace/context.json'))
c['entries']=[x for x in c['entries'] if x['id'].startswith('n')]
c['entries'].append({'id':'n9','role':'note','body':'R9: board.md:3 Thread A resolved. :4 Thread B revised DISK_PRESSURE (checkout-api,payments-svc). :5 Thread C ledger-svc failures cause unknown, ongoing (suspect CHG-113 db.pool_max=0 -> BAD_CONFIG_ROLLOUT, round-01/changes.md:3). :6 OPEN VENDOR_TICKET. changes.md:3 CHG-163 irrelevant.'})
json.dump(c,open('/task/workspace/context.json','w'))