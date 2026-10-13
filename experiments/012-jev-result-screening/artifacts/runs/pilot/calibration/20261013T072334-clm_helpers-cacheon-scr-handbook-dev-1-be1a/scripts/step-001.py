import os
d='/task/fixtures/handbook/'
for f in sorted(os.listdir(d)):
    l=open(d+f).read().split('\n')
    print(f,l[0][:150])