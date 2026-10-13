import json,re
L=[(i,l.strip()[:110]) for i,l in enumerate(open('/task/fixtures/round-05/logs/shipping-svc.log'),1) if 'tls' in l or 'cert' in l]
print(len(L),L[0][0],L[-1][0])
c=json.load(open('/task/workspace/context.json'))
e=c['entries'][0]
e['body']+='\nR5: board round-05/board.md:3 Thread B +notify-worker; :4 Thread D CERT_EXPIRED shipping-svc ongoing (logs confirm tls certificate_expired peer=bank-api shipping-svc.log:%d-%d, n=%d); :5 follow-up OPEN VENDOR_TICKET. DNS errs continue inventory-svc.log:22-75, ledger-svc.log:17-68. disk WARN 92-98%% notify-worker/shipping-svc still no errors. search-api 0.'%(L[0][0],L[-1][0],len(L))
c['entries']=[e]
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')