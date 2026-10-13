import json,sys,glob
sys.path.insert(0,'/task/fixtures')
note='Q1: 2026-03-15 -> HB-03 §2 36 c/km (superseded 2026-04-01 by HB-24 32); check HB-10 group exc (petrol?). Q2: HB-23 §2 2500; HB-18 §2 another country 5250 (check probation/months carve-out in HB-18). Q3: HB-39 §2 375; check HB-08.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':note}]},open('/task/workspace/context.json','w'))
import re
for f in ['HB-10','HB-18','HB-08']:
    t=open(f'/task/fixtures/handbook/{f}.md').read()
    print(f,t[:200]);[print(l[:260]) for l in t.split('\n') if re.search(r'\d',l) and ('##' in l or 'EUR' in l or 'cent' in l or 'month' in l)]
from handbook_tools import search
for q in ['meal allowance intern client-site','training budget team lead','purchase approval threshold facilities']:
    r=open(sorted(glob.glob('/task/workspace/search-results/*'))[-1]).read() if 0 else None
    search(q,k=8)
for p in sorted(glob.glob('/task/workspace/search-results/*'))[3:]:
    for l in open(p):
        if l.startswith('==='): h=l[4:60]+l[l.find('status'):l.find('status')+60]
        elif any(w in l for w in ['EUR','instead']): print(h.strip(),'|',l.strip()[:200])