import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' Memos HB-33 §2 London/Paris client-site 84; HB-03 §2; HB-39 §2 EV 46.'
json.dump(c,open('/task/workspace/context.json','w'))
for n in [33,3,39,25,26,9,22,18,37,32,11,27]:
    t=open(f'/task/fixtures/handbook/HB-{n:02d}.md').read()
    print('==',n,t.split('\n')[1][:150])
    for s in re.split(r'\n(?=§)',t)[1:]:
        if s.startswith('§1'):continue
        print(s.split('\n')[0],'|',re.sub(r'\s+',' ',s.split('\n',1)[1])[:160])
