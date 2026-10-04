open('/task/workspace/notes.txt','w').write('s1: RN 7.25.4 line5 timeout 2500->750, line13 pool 48->12. deploy line4 08:13:27. log143 timeouts 750ms, log184 pool wait 12/12\n')
import collections,re
b='/task/fixtures/stage-1/logs/'
for f in ['shipping-api.log','ingress-a.log']:
  c=collections.Counter();first={}
  for i,l in enumerate(open(b+f),1):
    if 'ERROR' in l or ' 5' in l[60:]:
      k=re.sub(r'[0-9a-f]{6,}|\d+','N',l[24:])[:70]
      c[k]+=1;first.setdefault(k,i)
  for k,v in c.most_common(8):print(f,first[k],v,k)