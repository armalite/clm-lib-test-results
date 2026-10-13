import json
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Docs: meals 01,33,26,35memo; car 03,24,38,10memo; homeoffice 05,28,39,08memo; training 09,32,27,30memo; procurement 11,15,25,22memo; reloc 16,19,23,18memo; FAQ 02, glossary 36'}]}
json.dump(c,open('/task/workspace/context.json','w'))
d='/task/fixtures/handbook/'
for n in ['03','24','10','38']:
    t=open(d+'HB-'+n+'.md').read()
    print(t[:1500]);print('====')
