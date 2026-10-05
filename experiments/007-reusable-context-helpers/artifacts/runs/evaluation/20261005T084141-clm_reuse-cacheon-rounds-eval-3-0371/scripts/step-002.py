import ctx,os
r='/task/fixtures/round-01/'
print(open(r+'changes.md').read()[:1500])
for f in sorted(os.listdir(r+'logs')):
  for i,l in enumerate(open(r+'logs/'+f)):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l and 'certificate_expired' not in l: print(f,i+1,l[:140].strip())
ctx.reset(['ctx.py has load/save/reset(notes). R1: board empty. ledger-svc CERT_EXPIRED peer=sso.example.net round-01/logs/ledger-svc.log:14-21 (many more). slow query WARNs everywhere are noise.'])