import os,re
d='/task/fixtures/handbook/'
for f in sorted(os.listdir(d)):
    t=open(d+f).read().splitlines()
    print(f,t[0][:150])
