import re,glob,os
d='/task/fixtures/round-06/'
print(open(d+'board.md').read());print(open(d+'changes.md').read())
noise=re.compile(r'request ok|health ok|heartbeat|gc cycle|slow query')
out=[]
for f in sorted(glob.glob(d+'logs/*.log')):
    seen={}
    for i,l in enumerate(open(f),1):
        if noise.search(l): continue
        m=re.sub(r'\d+','#',l.split(' ',2)[-1] if ' ' in l else l)[:70]
        seen.setdefault(m,[]).append(i)
    for m,ls in seen.items(): out.append('%s %d %d %d %s'%(os.path.basename(f),ls[0],ls[-1],len(ls),m.strip()))
print('\n'.join(out))
open('/task/workspace/notes.md','a').write('\nR6 logs:\n'+'\n'.join(out)+'\n')