import json,glob,re
d=json.load(open('/task/workspace/context.json'))
n=[e for e in d['entries'] if e['id']=='n1'][0]
n['body']+=' R5: board.md:3 Thread A mitigated; board.md:4 Thread B +checkout-api; board.md:5 OPEN CAPACITY_REVIEW; changes.md:4 CHG-143 APPLIED thread A mitigation auth-svc; CHG-138 TLS noise.'
d['entries']=[n]
json.dump(d,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  c={}
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|429|exhaust|max_inflight|expired|DNS|lag|OOM|disk',l,re.I):
      k=re.sub(r'\d+','#',l[20:110]);
      if k not in c: c[k]=i;print(f.split('/')[-1],i,l.strip()[:150])