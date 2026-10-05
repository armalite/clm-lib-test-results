L=open('/task/fixtures/round-07/logs/inventory-svc.log').read().splitlines()
for i,l in enumerate(L,1):
  if 'tls' in l:print(i,l[:200]);break
open('/task/workspace/notes.md','a').write('\nR7: Thread D CERT_EXPIRED inventory-svc ongoing (round-07/board.md:4); logs tls handshake failed round-07/logs/inventory-svc.log:7-68. Thread B adds pricing (round-07/board.md:3). CHG-151 PROPOSED.\n')