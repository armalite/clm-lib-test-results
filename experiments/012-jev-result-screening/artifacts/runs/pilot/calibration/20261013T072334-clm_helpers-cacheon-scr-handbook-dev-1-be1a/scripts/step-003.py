import json,re
c={'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':'Docs: HB-03 lodging memo: Zurich/Geneva/Oslo 270 (§2), not contractors (§3); base HB-22. HB-09 home-office memo: medical plan 750, carve-out part-time<20h; base HB-11 v3 eff 2026-03-01 500 (§2) +150 remote 4+ days (§3), supersedes HB-32 (check HB-32 for 2026-02-15). HB-13 lodging superseded 210. Other relevant: meals 17,27,33; training 18,23,26; mobile 20,25,31,37; car 29,38,39. Today=2026-10-13.'}]}
json.dump(c,open('/task/workspace/context.json','w'))
d='/task/fixtures/handbook/'
for n in [32,22,17,27,33,18,23,26,31,37,25,29,38,39]:
    t=open(d+'HB-%02d.md'%n).read().split('\n')
    print('==',n,t[2][:120])
    for l in t:
        if l.startswith('§'):print(l)
        elif re.search(r'\d+ (EUR|cents)|not apply|instead',l):print(' ',re.split(r'(?<=\.) ',l)[0][:230])
