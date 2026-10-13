import os,json
d='/task/fixtures/handbook/'
for n in [3,9,11,13,17,18,20,22,23,24,25,26,27,29,30,31,32,33,34,37,38,39,4,5]:
    t=open(d+'HB-%02d.md'%n).read()
    print('==',n,t[:1500].replace('\n\n','\n'))
