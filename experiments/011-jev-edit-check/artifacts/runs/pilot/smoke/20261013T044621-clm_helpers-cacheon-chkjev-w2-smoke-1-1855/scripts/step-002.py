import json
p='/task/workspace/context.json'
c=json.load(open(p))
c['entries'].append({'id':'note.stage1','role':'note','body':'Stage1 reqs: export_records(records,user,params)->str. CSV via csv.writer default dialect, lineterminator=\'\\n\', header id,title,owner,amount; rows ascending id; amount as given; empty -> header only. Do not modify input. Permissions: role viewer -> PermissionError; admin all projects; other roles only records with project in user[\'projects\'] (others silently dropped). Ignore unknown params. OBLIGATION (stays unless withdrawn): if later format is not CSV, every export must include top-level field "exported_by"=user[\'name\'].'})
json.dump(c,open(p,'w'))
print(open('/task/workspace/exporter/core.py').read());print(open('/task/workspace/exporter/__init__.py').read())
print(open('/task/fixtures/current-tests/test_stage.py').read()[:2500])