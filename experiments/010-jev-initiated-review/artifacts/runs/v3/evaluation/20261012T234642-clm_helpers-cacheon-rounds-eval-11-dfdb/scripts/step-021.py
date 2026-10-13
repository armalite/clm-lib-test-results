import re,json
f='/task/fixtures/round-07/logs/pricing-svc.log'
h=[i for i,l in enumerate(open(f),1) if re.search('mem|oom|restart|heap|rss',l,re.I)]
print(h)
for i,l in enumerate(open(f),1):
  if i in h[:2]:print(l.strip()[:200])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'].startswith('n')]
c['entries'].append({'id':'n7','role':'note','body':'R7: Thread B revised to DNS_RESOLUTION (round-07/board.md:3). Thread D MEMORY_LEAK pricing-svc ongoing (round-07/board.md:4). CHG-153 PROPOSED noise. DNS kms.internal continues round-07/logs/inventory-svc.log:1,3,21,29,31,59,65. pricing mem lines: '+str(h)+'. Next: advance to R8.'})
json.dump(c,open('/task/workspace/context.json','w'))