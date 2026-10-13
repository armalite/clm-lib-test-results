import json,re
n1='Docs: meals 01,33,26,35memo; car 03,24,38,10memo; homeoffice 05,28,39,08memo; training 09,32,27,30memo; procurement 11,15,25,22memo; reloc 16,19,23,18memo. Q1=36c HB-03 §2. HO: HB-08 memo medical 675 n/a. Reloc: HB-18 §2 abroad 5250 but §3 not within first 6 months -> standard HB-23 §2.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n1}]},open('/task/workspace/context.json','w'))
d='/task/fixtures/handbook/'
for n in ['39','23','01','33','26','35','09','32','27','30','11','15','25','22']:
    t=open(d+'HB-'+n+'.md').read().split('\n')
    print(t[0][:60]);print(t[1])
    for l in t[2:]:
        if re.search(r'\d',l):print(' ',l[:200])
    print('==')
