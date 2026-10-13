import json
summ='''Requirements in force (stage1+2), all implemented in /task/workspace/exporter/core.py, stage-1 and stage-2 visible tests pass:
- export_records(records,user,params)->str; do not modify input; ignore unknown params; ascending id order.
- Format CSV: header id,title,owner,amount; csv.writer default dialect, lineterminator='\\n'; id as int, amount as given; no records -> header only.
- Permissions: role 'viewer' -> PermissionError; 'admin' sees all projects; other roles only records with project in user['projects'] (others silently skipped).
- Status: only 'active' unless params.get('include_archived') is True (then 'archived' too).
- Confidential (stage2): confidential True never exported, except role 'admin' and params.get('purpose')=='audit' (other rules still apply).
- Date filter (stage2): params 'since' YYYY-MM-DD -> only created >= since.
- Compliance obligation (stage2, still active): if a later stage changes format from CSV, every export in the new format must include top-level field "exported_by" = user['name'], unless a later stage withdraws it.
Next: advance to stage 3.'''
c={'format':'clm-context/v1','entries':[{'id':'sum.s1-2','role':'summary','body':summ}]}
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')