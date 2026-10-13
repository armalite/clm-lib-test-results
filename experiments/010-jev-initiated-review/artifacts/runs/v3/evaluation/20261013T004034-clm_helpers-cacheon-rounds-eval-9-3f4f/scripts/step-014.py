import json
d=json.load(open('/task/workspace/context.json'))
n=[e for e in d['entries'] if e['id']=='n1'][0]['body']
n+='\nR5: board.md:3 Thread B adds notify-worker (cause DB_POOL unchanged, logs show disk usage notify-worker.log:2-57 shipping-svc.log:4-76). board.md:4 Thread D CERT_EXPIRED shipping-svc ongoing, real: shipping-svc.log:1-65 tls handshake bank-api certificate_expired. board.md:5 OPEN VENDOR_TICKET. DNS continues inventory-svc.log:22-75 ledger-svc.log:17-68. search-api clean. Next: advance R6.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))
print('ok')