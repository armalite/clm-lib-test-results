import json
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' Values: Q1 HB-32 400; Q2 HB-33 84 (check intern); Q3 HB-18 1150+550; Q4 HB-22 150; Q5 HB-39 46; Q6 HB-37 40+16.'
json.dump(c,open('/task/workspace/context.json','w'))
for n in [33,3,4,5,24,30,34,39,25,26]:
    t=open(f'/task/fixtures/handbook/HB-{n:02d}.md').read()
    print(n,t[:700].replace('\n',' | '))
