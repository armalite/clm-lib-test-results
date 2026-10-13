import os,collections
d='/task/fixtures/round-07/logs/'
for f in sorted(os.listdir(d)):
  c=collections.Counter();ex={}
  for i,l in enumerate(open(d+f),1):
    if 'ERROR' in l or 'error' in l:
      k=l[l.find('msg'):][:70] if 'msg' in l else l[40:110]
      c[k]+=1;ex.setdefault(k,[]).append(i)
  for k,v in c.most_common(3):print(f,v,k,ex[k][:5])