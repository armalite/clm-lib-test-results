import collections
b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md']:
 print(f);[print(i,l.rstrip()) for i,l in enumerate(open(b+f),1)]
L=open(b+'logs/payments-api.log').readlines()
c=collections.Counter(' '.join(l.split()[4:7]) for l in L if ' ERROR ' in l or ' WARN ' in l);print(c.most_common(6))
for i,l in enumerate(L,1):
 if ' ERROR ' in l:print(i,l.strip()[:170]);break
print(open(b+'metrics/payments-api.csv').readlines()[:2])