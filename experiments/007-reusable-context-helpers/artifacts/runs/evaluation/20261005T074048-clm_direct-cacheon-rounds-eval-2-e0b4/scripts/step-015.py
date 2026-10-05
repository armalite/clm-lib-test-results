import json,re,glob
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3','n4')]
json.dump(c,open('/task/workspace/context.json','w'))
for i,l in enumerate(open('/task/fixtures/round-05/board.md'),1):print(i,l.rstrip())
for f in sorted(glob.glob('/task/fixtures/round-05/logs/*')):
  n=0
  for i,l in enumerate(open(f),1):
    if re.search(r'ERROR|WARN|error',l):
      n+=1
      if n<=4:print(f[-18:],i,l.rstrip()[:110])
  print(f[-18:],'count',n)