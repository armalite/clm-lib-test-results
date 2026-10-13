import json,re,glob
notes='Docs: lodging HB-13,22,34,03memo; meals HB-17,27,04,33memo; training HB-18,23,05,26memo; home-office HB-11(v3 eff 2026-03-01 supersedes HB-32),32,24,09memo(medical 750, carve-out part-time); mobile HB-20,31,37,25memo; car HB-29,30,38,39memo. HB-03: Zurich/Geneva/Oslo 270, not contractors.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':notes}]},open('/task/workspace/context.json','w'))
for n in [11,32,13,22,17,27,33,18,23,26,20,31,37,25,29,38,39]:
    t=open(f'/task/fixtures/handbook/HB-{n:02d}.md').read().split('\n')
    print(n,t[1][:110])
    for l in t:
        if re.search(r'\d+ (EUR|cents)',l): print('  ',re.split(r'(?<=\.) ',l)[0][:230])
