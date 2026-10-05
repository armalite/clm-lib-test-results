import glob
b='/task/fixtures/round-01/'
print(open(b+'changes.md').read()[:1500])
for f in sorted(glob.glob(b+'logs/*')):
  for i,l in enumerate(open(f).read().splitlines(),1):
    if ('ERROR' in l or 'WARN' in l) and 'slow query' not in l and 'certificate_expired' not in l:print(f.split('/')[-1],i,l[:150])
open('/task/workspace/notes.md','w').write('R1: ledger-svc CERT_EXPIRED sso.example.net round-01/logs/ledger-svc.log:14-72 ; slow query WARN is noise everywhere\n')