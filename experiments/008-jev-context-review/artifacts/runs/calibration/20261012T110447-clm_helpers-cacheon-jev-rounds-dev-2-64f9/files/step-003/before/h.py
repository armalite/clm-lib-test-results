
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
        if hits: out.append(rel+'
 '+'
 '.join(hits))
    return '
'.join(out)
def setctx(entries):
    json.dump({'format':'clm-context/v1','entries':entries},open('/task/workspace/context.json','w'))
