b='/task/fixtures/round-09/logs/'
for f,ls in [('checkout-api.log',[34,55]),('payments-svc.log',[34,42]),('notify-worker.log',[3,5,12,67])]:
  L=open(b+f).read().splitlines()
  for i in ls:print(f,i,L[i-1][:160])