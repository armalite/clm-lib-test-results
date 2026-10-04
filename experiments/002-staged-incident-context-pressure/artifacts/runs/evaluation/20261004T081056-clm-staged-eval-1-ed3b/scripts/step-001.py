import os,re
b='/task/fixtures/stage-1/'
for f in ['UPDATE.md','config/quotes-api.yaml','deploy/deploys.log','deploy/release-notes-8.19.0-ff7b.md','ops/oncall-notes.md']:
  print('##',f)
  for i,l in enumerate(open(b+f),1):print(i,l.rstrip())
for f in ['logs/api-gateway.log','logs/quotes-api.log']:
  print('##',f)
  for i,l in enumerate(open(b+f),1):
    if re.search('ERROR|WARN|timeout|pool',l,re.I) and i%1==0:
      print(i,l.rstrip()[:160])
      if i>0: pass
