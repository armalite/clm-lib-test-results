import os
os.chdir('/task/fixtures')
for f in ['config/payments-api.yaml','deploy/changes.log','ops/oncall-notes.md']:
  for i,l in enumerate(open(f),1): print(f,i,l.rstrip()[:160])
import re,collections
for f in ['logs/front-proxy.log','logs/payments-api.log']:
  c=collections.Counter()
  for i,l in enumerate(open(f),1):
    if re.search('ERROR|WARN|timeout|fail',l,re.I):
      k=re.sub(r'\d+','N',l)[20:110]
      if c[k]<1: print(f,i,l.rstrip()[:200])
      c[k]+=1
  print(c.most_common(5))
L=open('metrics/pricing-core-latency.csv').readlines();print(L[:4],L[-3:])