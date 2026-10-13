import json
s1=json.load(open('/task/workspace/context.json'))['entries'][0]['body'].replace(' Next: advance to stage 2.','')
b2="Stage 2 rules: [NEW Status] only status 'active' exported, unless params.get('include_archived') is True; then 'archived' also exported. [NEW Compliance obligation] if a later stage changes export format from CSV, every export in new format must include top-level field \"exported_by\" = user['name']; stays in force unless later stage withdraws it. Implemented status filter in core.py loop (after confidential check); stage 2 visible tests 2/2 OK. Next: advance to stage 3."
c={'format':'clm-context/v1','entries':[{'id':'sum1','role':'summary','body':s1},{'id':'sum2','role':'summary','body':b2}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')