import re,collections
b='/task/fixtures/stage-2/'
for f in ['UPDATE.md','deploy/changes.log','ops/oncall-notes.md']:
  print(f);[print(i,l.rstrip()) for i,l in enumerate(open(b+f),1)]
L=open(b+'logs/quotes-api.log').readlines()
c=collections.Counter(re.sub(r'[0-9a-f]{6,}|\d+','N',l[30:])[:90] for l in L if 'ERROR' in l or 'WARN' in l)
for k,v in c.most_common(6):print(v,k)
n=[i for i,l in enumerate(L,1) if 'pool' in l.lower()];print(n[:2],L[n[0]-1][:200] if n else '')
print(open(b+'metrics/quotes-api.csv').readlines()[:3])