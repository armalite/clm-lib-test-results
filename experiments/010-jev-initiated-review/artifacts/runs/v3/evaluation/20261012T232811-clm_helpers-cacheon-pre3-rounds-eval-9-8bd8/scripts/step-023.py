import json
e=json.load(open('/task/workspace/context.json'))['entries']
keep=[x for x in e if x['id'] in('n1','n2','n3','n4')]
keep.append({'id':'n5','role':'note','body':'Round5: board: Thread B (DB_POOL shipping) now also notify-worker (round-05/board.md:3); Thread D opened CERT_EXPIRED shipping-svc ongoing (round-05/board.md:4); Follow-up OPEN VENDOR_TICKET (round-05/board.md:5). No changes.md. Logs: shipping-svc tls handshake failed peer=bank-api certificate_expired round-05/logs/shipping-svc.log:1,4,5,7,9,11,17,18 (plus disk lines mixed); notify-worker disk 96% round-05/logs/notify-worker.log:2,5,6,7,10,17,19,21; DNS geo.internal continues inventory/ledger. Still no db pool errors seen -> Thread B likely really DISK_PRESSURE. Next: advance to round 6.'})
json.dump({'format':'clm-context/v1','entries':keep},open('/task/workspace/context.json','w'))
print('ok')