print(open('/task/fixtures/round-12/board.md').read())
for s,k in [('checkout-api','config valid'),('ledger-svc','tls handshake'),('auth-svc','tls handshake'),('checkout-api','ERROR')]:
  L=open(f'/task/fixtures/round-12/logs/{s}.log').read().splitlines()
  print(s,k,[i+1 for i,l in enumerate(L) if k in l][:5])