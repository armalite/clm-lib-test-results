import json
d='/task/fixtures/handbook/'
for n in [32,11,22,13,3,17,27,33,18,23,26,31,37,25,29,38,39]:
    t=open(d+'HB-%02d.md'%n).read().split('\n')
    print(n,' | '.join(t[:2])[:200])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id']=='notes']
c['entries'][0]['body']+=' Amounts: HB-32 400(+150 remote); HB-22 150; HB-27 54, HB-33 Paris 84 not interns(§3); HB-18 1150+550 team lead(§3), HB-23 old 1450; HB-37 40+16 rotation(§3), HB-31 old 36; HB-29 34, HB-39 EV 46 (§2) not rental; HB-38 old 36.'
json.dump(c,open('/task/workspace/context.json','w'))