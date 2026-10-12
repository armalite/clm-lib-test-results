import json,glob,re
d=json.load(open('/task/workspace/context.json'))
n=[e for e in d['entries'] if e['id']=='n1'][0]
n['body']+=' R5 logs: checkout-api.log:21, payments-svc.log:13 429 fx-rates. R6: board.md:3 CLOSED ALERT_TUNING; board.md:4 OPEN CUSTOMER_COMMS; changes.md:3 CHG-147 retry budget (noise?).'
d['entries']=[n]
json.dump(d,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  c={}
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|429|exhaust|max_inflight|expired|DNS|lag|OOM|disk|stampede|miss',l,re.I):
      k=re.sub(r'\d+','#',l[20:110])
      if k not in c: c[k]=i;print(f.split('/')[-1],i,l.strip()[:150])