import ctx,os
ctx.setnote('n1','R1: changes.md:3 CHG-109 PROPOSED HPA search; :4 CHG-113 APPLIED search-api http.max_inflight=-1; :5 CHG-114 checkout no cfg. ledger-svc CERT_EXPIRED peer=sso.example.net round-01/logs/ledger-svc.log:14,15,21,39,72. slow query WARNs everywhere = noise. board r1 empty.')
ctx.keep_only(['n1'])
r='/task/fixtures/round-01/logs/'
for f in sorted(os.listdir(r)):
    if f in('checkout-api.log','inventory-svc.log','ledger-svc.log'):continue
    for i,l in enumerate(open(r+f),1):
        if 'slow query' not in l and any(k in l for k in('ERROR','WARN','429','fail')):print(f,i,l[:130].strip())