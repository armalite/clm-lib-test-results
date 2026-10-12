import json,re,glob
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']+='\nR7 logs: auth cert_expired (round-07/logs/auth-svc.log:12); checkout pool exhausted 16/16 (round-07/logs/checkout-api.log:2,8).\nR8: board.md:3 Thread D closed false alarm (but logs show real pool exhaustion?). changes:3 CHG-156 PROPOSED ignore.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-08/logs/*.log')):
  L=[(i,l) for i,l in enumerate(open(f),1) if re.search('ERROR|FATAL|expired|exhaust|disk',l,re.I)]
  print(f.split('/')[-1],len(L),[i for i,_ in L][:8])
  for i,l in L[:1]: print(' ',l.strip()[:160])