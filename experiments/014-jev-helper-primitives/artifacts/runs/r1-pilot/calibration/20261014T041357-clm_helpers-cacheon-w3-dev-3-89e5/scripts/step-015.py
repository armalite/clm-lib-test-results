import json,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
L=s.split('\n')
print(L[25:30])
s=s.replace("    doc = {'records': recs, 'exported_by': user.get('name')}","    doc = {'records': recs}\n    if role != 'admin':\n        doc['exported_by'] = user.get('name')")
open(p,'w').write(s)
c=json.load(open('/task/workspace/context.json'))
reg=c['entries'][0]['body']
reg=reg.replace("CURRENT [S2.3] params max_records int>=1: first N by ascending id after all other rules.","CURRENT [S2.3, S6.2] params max_records int>=1: first N by ascending id after all other rules; values above 30 treated as 30.")
reg=reg.replace("must include top-level 'exported_by'=user['name'].","must include top-level 'exported_by'=user['name'], EXCEPT role admin: omit exported_by (S6.1).")
reg=reg.replace("CURRENT [S2.4]","CURRENT [S2.4, S6.1]")
reg+="\nHISTORY [S6.3] Note: web UI shows 50 records/page; no export change."
c['entries']=[{'id':'register','role':'summary','body':reg},{'id':'progress','role':'note','body':'Stages 1-6 exported_by done in core.py; max_records cap check pending (see step output).'}]
json.dump(c,open('/task/workspace/context.json','w'))