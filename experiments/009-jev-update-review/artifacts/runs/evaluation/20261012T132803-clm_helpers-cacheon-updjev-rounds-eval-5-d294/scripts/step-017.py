import json,re
for s in ['checkout-api','auth-svc','ledger-svc']:
  L=open(f'/task/fixtures/round-07/logs/{s}.log').read().splitlines()
  h=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('ERROR|exhaust|pool|cert',l)]
  print(s,len(h),h[:3],h[-1:] if h else '')
c=json.load(open('/task/workspace/context.json'))
n=[e for e in c['entries'] if e['id']=='n1'][0]
n['body']=n['body'].replace(' Next: advance to R7.','')+'\nR7: board.md:3 Thread A RESOLVED; :4 Thread B revised CERT_EXPIRED auth-svc (status ongoing); :5 OPEN ALERT_TUNING.'
c['entries']=[n]
json.dump(c,open('/task/workspace/context.json','w'))