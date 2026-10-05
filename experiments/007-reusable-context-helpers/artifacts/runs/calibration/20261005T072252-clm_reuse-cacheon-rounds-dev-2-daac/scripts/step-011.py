import re,glob,collections
print(open('/task/fixtures/round-04/board.md').read())
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
    c=collections.Counter();first={}
    for i,l in enumerate(open(f),1):
        if re.search(r'ERROR|error|FATAL',l):
            k=re.sub(r'\d+','N',l)[30:110];c[k]+=1;first.setdefault(k,[i,i]);first[k][1]=i
    print(f.split('/')[-1]);[print(' ',v,first[k],k) for k,v in c.most_common(3)]
    print(' sample:',open(f).readline()[:150])