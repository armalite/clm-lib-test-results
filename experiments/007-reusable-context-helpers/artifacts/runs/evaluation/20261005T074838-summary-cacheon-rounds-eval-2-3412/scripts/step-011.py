import glob
out=[]
for n in ['board.md','changes.md']:
    for i,l in enumerate(open('/task/fixtures/round-04/'+n),1): out.append(f'{n} {i} {l.rstrip()[:300]}')
for f in sorted(glob.glob('/task/fixtures/round-04/logs/*.log')):
    c=0
    for i,l in enumerate(open(f),1):
        if 'heap usage' in l: c+=1
        if any(k in l for k in ['slow query',' INFO ','heap usage','gc cycle','request ok','health ok','heartbeat']): continue
        out.append(f"{f.split('/')[-1]} {i} {l.strip()[:140]}")
    out.append(f"{f.split('/')[-1]} heap={c}")
print('\n'.join(out[:60]))
open('/task/workspace/r4.txt','w').write('\n'.join(out))
