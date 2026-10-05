import json
notes=open('/task/workspace/notes.txt').read()+'\nR3: board empty; CHG-125 APPLIED retry budget=1 (round-03/changes.md:3). cert errs continue inventory round-03/logs/inventory-svc.log:9-39, ledger round-03/logs/ledger-svc.log:23-40. others clean.'
open('/task/workspace/notes.txt','w').write(notes)
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':notes}]},open('/task/workspace/context.json','w'))
print('ok')