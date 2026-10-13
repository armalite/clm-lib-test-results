import os,re,json
p='/task/fixtures/round-09'
for f in ['board.md','changes.md']:print(f,open(p+'/'+f).read())
for f in sorted(os.listdir(p+'/logs')):
  L=[(i+1,l) for i,l in enumerate(open(p+'/logs/'+f)) if not re.search('slow query|request ok|heartbeat|gc |health ok',l)]
  print(f,len(L),L[0][0] if L else '',L[-1][0] if L else '',L[0][1][:150] if L else '')
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
json.dump(c,open('/task/workspace/context.json','w'))