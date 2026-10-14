import json
print(open('/task/workspace/exporter/core.py').read());print(open('/task/workspace/exporter/__init__.py').read())
print(open('/task/fixtures/current-tests/test_stage.py').read()[:2500])
reg='''CURRENT [S1.1] Format: CSV via csv.writer default dialect, lineterminator \\n; header id,title,owner,amount; rows ascending id; no records -> header only.
CURRENT [S1.2] Scope: role 'admin' any project; others only records with project in user['projects'], silently skipped.
CURRENT [S1.3] Status: only 'active' unless params.get('include_archived') is True -> archived too.
CURRENT [S1.4] params 'since' YYYY-MM-DD: only created >= since.
CURRENT [S1.5] Title stripped of leading/trailing whitespace.
CURRENT [S1.0] API export_records(records,user,params)->str; record keys id,title,owner,project,status,amount(str keep exact),confidential,created,region,optional updated; don't modify input; ignore unknown params.
HISTORY [S1.6] Decision: date filter introduced for monthly reconciliation runs.'''
json.dump({'format':'clm-context/v1','entries':[{'id':'register','role':'summary','body':reg}]},open('/task/workspace/context.json','w'))