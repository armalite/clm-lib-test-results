import json
c=json.load(open('/task/workspace/context.json'))
e=[x for x in c['entries'] if x['id'] in('n1','n2')]
e.append({'id':'n3','role':'note','body':'R3: board empty (no change). changes.md:3 CHG-124 PROPOSED (ignore). Lag WARNs payments(3-55) ledger(20-61) still fluctuating 20k-87k, no errors elsewhere. Next: advance to R4.'})
c['entries']=e
json.dump(c,open('/task/workspace/context.json','w'))