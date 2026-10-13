import json
e=json.load(open('/task/workspace/context.json'))['entries']
keep=[x for x in e if x['id'] in('n1','n2','n3','n4','n5')]
keep.append({'id':'n6','role':'note','body':'Round6: board: Thread A (DNS ledger/inventory) mitigated (round-06/board.md:3); Follow-up OPEN RUNBOOK_UPDATE (round-06/board.md:4). changes: CHG-142 APPLIED retry budget GETs=1 (round-06/changes.md:3); CHG-150 APPLIED mitigation thread A ledger-svc (round-06/changes.md:4). Logs: no DNS errors in inventory/ledger anymore; search-api no errors; notify-worker disk 93-97% round-06/logs/notify-worker.log:12,14,48,52,72,78; shipping-svc cert_expired bank-api + disk mixed round-06/logs/shipping-svc.log:1,13,17,22,23,26,30,40,42,48,58,65,69,70,77,86. Next: advance to round 7.'})
json.dump({'format':'clm-context/v1','entries':keep},open('/task/workspace/context.json','w'))
print('ok')