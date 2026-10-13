import json
p='/task/workspace/context.json'
c=json.load(open(p))
n=c['entries'][0]['body']+"\nR5: board round-05/board.md:3 Thread B adds notify-worker (cause DB_POOL unchanged); :4 Thread D CERT_EXPIRED shipping-svc ongoing; :5 follow-up OPEN VENDOR_TICKET. shipping tls certificate_expired peer=bank-api round-05/logs/shipping-svc.log:1 (check other lines). DNS continues inventory round-05/logs/inventory-svc.log:22-75, ledger round-05/logs/ledger-svc.log:17-68. disk WARNs notify round-05/logs/notify-worker.log:2-57. search-api no errors."
c['entries']=[{'id':'n1','role':'note','body':n}]
json.dump(c,open(p,'w'))
print('ok')