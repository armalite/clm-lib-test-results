import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Docs: meals 01,33,26,35memo; car 03,24,38,10memo; homeoffice 05,28,39,08memo; training 09,32,27,30memo; procurement 11,15,25,22memo; reloc 16,19,23,18memo; FAQ 02, glossary 36. Q1=36 cents (HB-03 §2, superseded 2026-04-01 by HB-24 32c; EV memo HB-10 n/a petrol).'}]}
json.dump(c,open('/task/workspace/context.json','w'))
import re
d='/task/fixtures/handbook/'
for n in ['05','28','08','16','19','18']:
    t=open(d+'HB-'+n+'.md').read().split('\n')
    print(t[0]);print(t[1])
    for l in t:
        if l.startswith('§'):continue
        if re.search(r'\d',l) and not l.startswith('version'):print(' ',l.split('. ')[0])
    print('==')
