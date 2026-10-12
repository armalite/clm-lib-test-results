import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]
json.dump(c,open('/task/workspace/context.json','w'))
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-04/'+f),1):print(f,i,l.rstrip()[:200])
import glob,re,collections
for p in sorted(glob.glob('/task/fixtures/round-04/logs/*')):
  d=collections.defaultdict(list)
  for i,l in enumerate(open(p),1):
    if re.search(r'ERROR|WARN|FATAL',l,re.I):
      k=re.sub(r'[0-9]','',l.split(' ',1)[-1])[:70];d[k].append(i)
  for k,v in d.items():print(p.split('/')[-1],v[:8],len(v),k)