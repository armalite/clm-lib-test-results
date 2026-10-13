import json,re,glob,os
d=json.load(open('/task/workspace/context.json'))
for e in d['entries']:
  if e['id']=='notes': e['body']+="\nR7 logs: WARN slow query is noise. inventory-svc 429 fx-rates continues. Filter by level ERROR only."
d['entries']=[e for e in d['entries'] if e['id']=='notes']
json.dump(d,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*.log')):
  h=[(i,l) for i,l in enumerate(open(f),1) if re.search(r'ERROR|FATAL|CRIT',l,re.I)]
  msgs=set(re.sub(r'.*"msg":"([^"]*)".*?("upstream":"[^"]*")?.*',r'\1 \2',l.strip()) for i,l in h)
  print(os.path.basename(f),len(h),h[0][0] if h else '',h[-1][0] if h else '',list(msgs)[:3])