import re,collections
b='/task/fixtures/stage-2/'
for f in ['UPDATE.md','deploy/changes.log','ops/oncall-notes.md']:
  for i,l in enumerate(open(b+f),1): print(f,i,l.rstrip())
for f in ['logs/quotes-api.log','logs/api-gateway.log']:
  c=collections.Counter();first={}
  for i,l in enumerate(open(b+f),1):
    if re.search('ERROR|WARN|503',l):
      k=re.sub(r'\d+','N',l.split(' ',2)[-1])[:90];c[k]+=1;first.setdefault(k,i)
  for k,v in c.most_common(6): print(f,first[k],v,k)
print(open(b+'metrics/quotes-api.csv').read()[:400])