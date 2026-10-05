import os,json,re,collections
b='/task/fixtures/round-08/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):
    if l.strip(): print(f,i,l.rstrip())
for f in sorted(os.listdir(b+'logs')):
  g=collections.OrderedDict()
  for i,l in enumerate(open(b+'logs/'+f),1):
    l=l.strip()
    try:
      d=json.loads(l);lv=d.pop('level');d.pop('ts',None);d.pop('svc',None);m=d.pop('msg');ex=str({k:v for k,v in d.items() if k not in('ms','table')})
    except Exception:
      p=l.split(None,3);lv=p[1] if len(p)>1 else '?';m=re.sub(r'\d+','N',p[3] if len(p)>3 else l);ex=''
    if lv=='INFO' or 'slow query' in m: continue
    k=(lv,m,ex);g.setdefault(k,[0,i,i]);g[k][0]+=1;g[k][2]=i
  for k,v in g.items(): print(f,k,v)