import re,collections
b='/task/fixtures/stage-1/logs/'
for f in ['returns-svc.log','edge-gw.log']:
 c=collections.Counter();first={}
 for i,l in enumerate(open(b+f),1):
  if 'ERROR' in l:
   k=re.sub(r'\d+','N',l[40:])[:90];c[k]+=1;first.setdefault(k,i)
 for k,v in c.most_common(5):print(f,first[k],v,k)
L=open(b+'returns-svc.log').readlines()
for i,l in enumerate(L,1):
 if 'pool' in l and 'ERROR' in l:print(i,l.strip());break
for i,l in enumerate(L,1):
 if 'tax-engine' in l and 'ERROR' in l:print(i,l.strip());break