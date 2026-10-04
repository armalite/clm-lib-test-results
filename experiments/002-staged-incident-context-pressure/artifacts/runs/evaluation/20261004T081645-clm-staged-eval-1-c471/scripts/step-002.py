import collections,re
b='/task/fixtures/stage-1/'
for f in ['logs/api-gateway.log','logs/quotes-api.log']:
 L=open(b+f).readlines()
 c=collections.Counter(re.sub(r'\d+','N',l[20:110]) for l in L)
 print(f);[print(v,k) for k,v in c.most_common(8)]
 for i,l in enumerate(L,1):
  if re.search(r'timeout|pool|exhaust|error|fail',l,re.I):print(i,l.rstrip()[:160]);break