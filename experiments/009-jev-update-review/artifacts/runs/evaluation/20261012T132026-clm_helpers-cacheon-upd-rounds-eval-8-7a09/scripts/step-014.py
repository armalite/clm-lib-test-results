import json,re,glob
c=json.load(open('/task/workspace/context.json'))
b=c['entries'][0]['body']
b+='\nR6: board.md:3 Thread A mitigated; board.md:4 Thread D DNS_RESOLUTION notify-worker ongoing. changes.md:4 CHG-150 APPLIED mitigation A pricing-svc; changes.md:3 CHG-147 noise.'
c['entries']=[{'id':'n1','role':'note','body':b}]
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  hits=[(i,l.strip()[:150]) for i,l in enumerate(open(f),1) if re.search(r'ERROR|WARN|error|fail',l)]
  print(f.split('/')[-1],len(hits))
  for h in hits[:4]: print(' ',h)