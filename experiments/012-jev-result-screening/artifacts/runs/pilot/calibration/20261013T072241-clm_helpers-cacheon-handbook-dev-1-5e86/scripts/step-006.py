import json,re
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']+=' Carve-outs: HB-33§3 interns->HB-27§2 standard; HB-03§3 contractors; HB-39§3 EV rental; HB-25 field eng; HB-26 security; HB-09 medical. Exceptions secs: HB-22§5,HB-18§5.'
json.dump(c,open('/task/workspace/context.json','w'))
for n in [27,32,11,29,38,30,17,4,20,31]:
    t=open(f'/task/fixtures/handbook/HB-{n:02d}.md').read()
    print('==',n,t.split('\n')[1][:120])
    for s in re.split(r'\n(?=§)',t)[1:]:
        if s[:2] in('§2','§3'):print(s.split('\n')[0],'|',re.sub(r'\s+',' ',s.split('\n',1)[1])[:110])
