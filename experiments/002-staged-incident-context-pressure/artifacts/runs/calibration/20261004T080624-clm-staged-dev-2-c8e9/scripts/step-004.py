import json,collections,re
b='/task/fixtures/stage-2/'
for f in ['deploy/changes.log','ops/oncall-notes.md']:
  print('==',f)
  for i,l in enumerate(open(b+f),1):print(i,l.rstrip())
L=open(b+'logs/catalog-api.log').readlines()
c=collections.Counter(re.sub(r'\d+','N',' '.join(l.split()[4:10])) for l in L if 'ERROR' in l)
print(c.most_common(5))
for i,l in enumerate(L,1):
  if 'ERROR' in l and 'ledger' not in l:print(i,l.rstrip()[:200]);break
M=open(b+'metrics/catalog-api.csv').readlines();print(M[0].strip(),M[-1].strip())
p='/task/workspace/context.json'
d={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1: deploy catalog-api 8.26.3-35fd at stage-1/deploy/deploys.log:5. Release notes stage-1/deploy/release-notes-8.26.3-35fd.md:11 ledger timeout 2500->800; :15 db.pool.max_size 60->10. config yaml pool 60 (line 11). stage1 log ledger timeouts 800ms e.g. stage-1/logs/catalog-api.log:144. Stage 2 released; reading it now.'}]}
json.dump(d,open(p,'w'))