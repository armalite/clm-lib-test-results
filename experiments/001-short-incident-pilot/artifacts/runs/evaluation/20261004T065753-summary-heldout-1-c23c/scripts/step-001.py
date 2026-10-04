import os
for f in ['certs/inventory.csv','config/payments-api.yaml','deploy/changes.log','ops/oncall-notes.md']:
    print('==',f)
    for i,l in enumerate(open('/task/fixtures/'+f),1): print(i,l.rstrip()[:160])