import os
b='/task/fixtures/'
for f in ['config/shipping-api.yaml','deploy/changes.log','ops/oncall-notes.md']:
  print('==',f)
  for i,l in enumerate(open(b+f),1): print(i,l.rstrip())