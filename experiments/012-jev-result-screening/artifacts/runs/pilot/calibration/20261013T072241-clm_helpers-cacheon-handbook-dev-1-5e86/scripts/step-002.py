import glob,re
for n in [3,4,5,9,11,13,17,18,20,22,23,24,25,26,27,29,30,31,32,33,34,37,38,39]:
    t=open(f'/task/fixtures/handbook/HB-{n:02d}.md').read()
    print('=====',n,t[:1400].replace('\n\n','\n'))
