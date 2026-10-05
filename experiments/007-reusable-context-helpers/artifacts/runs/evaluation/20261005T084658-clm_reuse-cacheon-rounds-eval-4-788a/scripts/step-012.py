import ctx
print(open('/task/fixtures/round-04/board.md').read())
L=open('/task/workspace/spill/s11.obs.txt').read().splitlines()
import collections
c=collections.Counter()
for l in L:
    p=l.split(' ',2)
    if len(p)==3:
        k=(p[0],p[2][20:70])
        c[p[0]]+=1
        if c[p[0]]<=3: print(l[:130])
print(c)
ctx.keep_notes(open('/task/workspace/context.json').read().split('"body": "',1)[1].split('"}',1)[0] if False else None) if False else None