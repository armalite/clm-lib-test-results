import json,re
n1='Docs: meals 01,33,26,35memo; car 03,24,38,10memo; homeoffice 05,28,39,08memo; training 09,32,27,30memo; procurement 11,15,25,22memo; reloc 16,19,23,18memo. Q1=36c HB-03 §2. Q2=2500 HB-23 §2, HB-18 §2,§3. Q3=375 HB-39 §2 (HB-08 medical n/a). Q4=60 HB-33 §2, HB-35 §2,§3 (intern carve-out).'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1}]},open('/task/workspace/context.json','w'))
d='/task/fixtures/handbook/'
for n in ['32','30','11','15','25','22']:
    t=open(d+'HB-'+n+'.md').read().split('\n')
    print(t[1][:90])
    for l in t[2:]:
        if re.search(r'\d',l) and not l.startswith('§'):print(' ',l[:150])
    print('==')
