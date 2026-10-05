import json
notes=open('/task/workspace/notes.txt').read()+'\nR2: board Thread A CERT_EXPIRED ledger-svc+inventory-svc ongoing (round-02/board.md:3); inventory errs round-02/logs/inventory-svc.log:10-13; ledger round-02/logs/ledger-svc.log:20-43. CHG-117 PROPOSED. search-api no errors yet r2.'
open('/task/workspace/notes.txt','w').write(notes)
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':notes}]},open('/task/workspace/context.json','w'))
print('ok')