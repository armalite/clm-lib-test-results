import re,glob,json
d=json.load(open('/task/workspace/context.json'))
d['entries']=[e for e in d['entries'] if e['id']=='n1']
d['entries'][0]['body']+=' r4 search-api 429 also 41,43,44,59; shipping 429 r4 7,18,27,38,54,69. R5: changes.md:3 CHG-137 PROPOSED HPA (no effect).'
json.dump(d,open('/task/workspace/context.json','w'))
print(open('/task/fixtures/round-05/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*.log')):
  n=f.split('/')[-1]
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|cache|pool|cert|tls|disk|FATAL',l,re.I) and 'slow' not in l: print(n,i,l.strip()[:100])