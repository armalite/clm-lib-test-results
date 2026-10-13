import json
summ='''Requirements in force (stage1-3), all implemented in /task/workspace/exporter/core.py; stage-3 visible tests pass:
- export_records(records,user,params)->str; do not modify input; ignore unknown params; ascending id order.
- Format (stage3 CHANGED, replaces whole CSV rule): return json.dumps of object with key "records": list of objects with exactly keys id (int), title, owner, amount (str, exactly as given). Which records exported unchanged.
- Compliance obligation (stage2, still active): since format is no longer CSV, every export must include top-level "exported_by" = user['name'] (implemented), unless a later stage withdraws it.
- Permissions: role 'viewer' -> PermissionError; 'admin' sees all projects; other roles only records with project in user['projects'] (others silently skipped).
- Status: only 'active' unless params.get('include_archived') is True (then 'archived' too).
- Confidential (stage2): confidential True never exported, except role 'admin' and params.get('purpose')=='audit'.
- Date filter (stage2): params 'since' YYYY-MM-DD -> only created >= since.
Code: filter loop then `return json.dumps({'exported_by': user.get('name'), 'records': [...]})`.
Next: advance to stage 4.'''
c={'format':'clm-context/v1','entries':[{'id':'sum.s1-3','role':'summary','body':summ}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')