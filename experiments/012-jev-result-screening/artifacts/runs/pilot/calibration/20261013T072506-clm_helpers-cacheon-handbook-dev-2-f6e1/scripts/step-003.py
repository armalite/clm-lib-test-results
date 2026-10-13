import json,sys,re
sys.path.insert(0,'/task/fixtures')
note='Q1: 2026-03-15 HB-03 §2 36 c/km (HB-24 32 from 2026-04-01); HB-10 §2 only EV 45 -> petrol 36. Q2: HB-18 §3 carve-out first 6 months -> HB-23 §2 2500 (cite HB-18 §2,§3). Q3: HB-39 §2 375 (HB-08 only medical). Q4: HB-35 §3 intern -> HB-33 §2 60 (cite HB-35 §2,§3). Q5: see SR-008 (HB-09,HB-32,HB-30). Q6: TODO.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':note}]},open('/task/workspace/context.json','w'))
from handbook_tools import search
import io,contextlib
with contextlib.redirect_stdout(io.StringIO()): search('purchase approval threshold facilities',k=8)
import glob
for p in sorted(glob.glob('/task/workspace/search-results/*'))[-2:]:
  for l in open(p):
    if l.startswith('==='): print(l[:150].strip())
    elif re.search(r'\d',l): print('  ',l.strip()[:170])