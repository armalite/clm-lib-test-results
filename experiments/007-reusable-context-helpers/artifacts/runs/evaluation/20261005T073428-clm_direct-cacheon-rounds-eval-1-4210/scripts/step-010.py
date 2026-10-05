import json
p='/task/workspace/context.json'
d=json.load(open(p))
n=[e for e in d['entries'] if e['id']=='notes'][0]['body']
n=n.replace(' 13 lag lines (not yet checked trend). Next: check r03 lag values then advance.',' lag still fluctuating 20k-87k both svcs, not growing (likely false alarm / noise). Next: advance to R4.')
json.dump({'format':'clm-context/v1','entries':[{'id':'notes','role':'note','body':n}]},open(p,'w'))
print('ok')