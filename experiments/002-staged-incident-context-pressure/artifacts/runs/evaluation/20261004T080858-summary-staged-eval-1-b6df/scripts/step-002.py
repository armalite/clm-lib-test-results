open('/task/workspace/notes.md','w').write('S1: rn 8.19.0-ff7b line9 risk-score timeout 2500->800; line15 db pool 60->14. qa log line206 timeout 800ms errors start 08:22.\n')
import re,collections
b='/task/fixtures/stage-1/logs/'
c=collections.Counter()
for f in ['quotes-api.log','api-gateway.log']:
  for i,l in enumerate(open(b+f),1):
    if 'ERROR' in l:
      k=f+re.sub(r'[0-9a-f]{10}|\d+','N',l[40:])[:70]
      if c[k]<1:print(f,i,l.rstrip()[:170])
      c[k]+=1
for k,v in c.items():print(v,k)