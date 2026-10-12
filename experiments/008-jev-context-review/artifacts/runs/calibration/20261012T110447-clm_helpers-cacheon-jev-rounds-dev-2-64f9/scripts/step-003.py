helper=r'''
import glob,json
def scan(r):
    out=[]
    base=f'/task/fixtures/round-{r:02d}/'
    for p in sorted(glob.glob(base+'*.md'))+sorted(glob.glob(base+'logs/*')):
        L=open(p).read().splitlines()
        rel=p.replace('/task/fixtures/','')
        hits=[]
        for i,l in enumerate(L,1):
            ll=l.lower()
            if p.endswith('.md'):
                if l.strip() and not l.startswith('# '):hits.append(f'{i}:{l[:150]}')
            elif 'slow query' not in ll and any(k in ll for k in ['error','warn','fail','429','crit','fatal']):hits.append(f'{i}:{l[:120]}')
        if p.endswith('.log') and len(hits)>6:
            hits=hits[:3]+[f'..({len(hits)} total)']+hits[-2:]
        if hits: out.append(rel+'\n '+'\n '.join(hits))
    return '\n'.join(out)
def setctx(entries):
    json.dump({'format':'clm-context/v1','entries':entries},open('/task/workspace/context.json','w'))
'''
open('/task/workspace/h.py','w').write(helper)
import h
h.setctx([{'id':'n1','role':'note','body':'R1: changes.md:3 CHG-107 APPLIED retry budget GETs=1. inventory-svc DNS SERVFAIL host=rates.internal (round-01/logs/inventory-svc.log:7,20,50-90). slow query WARNs everywhere = noise. Board empty. helper: import h; print(h.scan(r)); h.setctx(entries) (overwrites whole ctx)'}])
print(h.scan(1)[-1500:])