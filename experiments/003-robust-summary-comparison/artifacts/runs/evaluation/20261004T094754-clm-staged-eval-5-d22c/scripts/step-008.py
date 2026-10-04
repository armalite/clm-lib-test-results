import re
b='/task/fixtures/stage-3/'
for i,l in enumerate(open(b+'deploy/changes.log'),1):print(i,l.rstrip())
L=open(b+'logs/quotes-api.log').readlines()
x=[i for i,l in enumerate(L,1) if 'ERROR' in l];print(len(x),x[:3]);print(L[x[0]-1].rstrip())
I=open(b+'logs/ingress-a.log').readlines()
y=[i for i,l in enumerate(I,1) if 'status=5' in l];print(y[:3])
M=open(b+'metrics/quotes-api.csv').readlines();print(M[0],M[30],M[-1])