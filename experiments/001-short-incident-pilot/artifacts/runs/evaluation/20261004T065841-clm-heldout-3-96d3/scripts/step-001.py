import os
b='/task/fixtures/'
for f in ['config/inventory-svc.yaml','deploy/changes.log','flags/audit.log','flags/registry.json','ops/oncall-notes.md']:
  print('==',f)
  for i,l in enumerate(open(b+f),1):print(i,l.rstrip()[:160])