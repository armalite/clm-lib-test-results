import re
print(open('/task/fixtures/stage-3/deploy/changes.log').read())
L=open('/task/fixtures/stage-3/logs/payments-api.log').read().splitlines()
h=[i for i,l in enumerate(L,1) if 'pool' in l.lower() or 'ERROR' in l]
print(len(h));[print(i,L[i-1][:200]) for i in h[:4]]
M=open('/task/fixtures/stage-3/metrics/payments-api.csv').read().splitlines();print(M[0]);print(M[30])