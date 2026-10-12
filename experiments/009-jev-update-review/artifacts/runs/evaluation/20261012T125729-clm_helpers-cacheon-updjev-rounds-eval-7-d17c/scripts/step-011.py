b='/task/fixtures/round-04/logs/'
import os
for f in os.listdir(b):
    L=open(b+f).read().splitlines()
    print(f,len(L))
    for i,l in enumerate(L[:3]): print(i+1,l[:180])