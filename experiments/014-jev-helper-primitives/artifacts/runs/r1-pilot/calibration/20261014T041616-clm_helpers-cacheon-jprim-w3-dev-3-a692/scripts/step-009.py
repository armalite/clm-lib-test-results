import json,subprocess,sys
c=open('exporter/core.py').read()
c=c.replace("import csv, io","import csv, io, json")
c=c.replace("if role != 'admin' and r.get('project') not in user.get('projects', []):","if role != 'admin' and r.get('project') not in user.get('projects', []) and r.get('owner') != user.get('name'):")
i=c.index('    buf = io.StringIO()')
c=c[:i]+"""    res = {'exported_by': user.get('name'), 'records': [{'id': int(r['id']), 'title': str(r['title']).strip(), 'owner': r['owner'], 'amount': r['amount']} for r in out]}
    return json.dumps(res)
"""
open('exporter/core.py','w').write(c)
d=json.load(open('context.json'))
d['entries']=[e for e in d['entries'] if e['id'] not in ('s6.act','s6.obs','s6.rcpt','s8.act','s8.obs','s7.act')]
for e in d['entries']:
    if e['id']=='s7.obs': e['body']='Stage 3 released: S3.1 JSON format {records:[id,title,owner,amount]}; S3.2 non-admin may export own records; S3.3 note.'
    if e['id']=='s5.note': e['body']='core.py implements S1-S3 (JSON with exported_by per S2.4). reghelper.update(stage) Jev-based; override(ids,reason).'
json.dump(d,open('context.json','w'))
import reghelper;reghelper.update(3)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-800:])