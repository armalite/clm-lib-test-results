L=open('/task/fixtures/stage-3/logs/quotes-api.log').readlines()
x=[i for i,l in enumerate(L,1) if '22/22' in l];print(len(x),x[:2]);print(L[x[0]-1].rstrip() if x else '')