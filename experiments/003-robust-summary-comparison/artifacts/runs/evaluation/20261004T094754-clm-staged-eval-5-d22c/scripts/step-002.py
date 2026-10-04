import collections,re
b='/task/fixtures/stage-1/logs/'
L=open(b+'quotes-api.log').readlines()
c=collections.Counter(re.sub(r'\d+','N',' '.join(l.split()[4:9])) for l in L if 'ERROR' in l or 'WARN' in l);print(c.most_common(8))
for i,l in enumerate(L,1):
  if 'runtime' in l and ('ERROR' in l or 'WARN' in l):print(i,l.rstrip()[:200]);break
I=open(b+'ingress-a.log').readlines()
for i in (1,200,433):print(i,I[i-1].rstrip()[:200])