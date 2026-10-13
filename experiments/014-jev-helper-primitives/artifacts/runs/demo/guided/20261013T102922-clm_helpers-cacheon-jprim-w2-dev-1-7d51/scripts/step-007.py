import subprocess,sys,json
sys.path.insert(0,'/task/workspace')
p='/task/workspace/exporter/core.py'
s=open(p).read()
i=s.index('    buf = io.StringIO()')
s=s[:i]+"    return json.dumps({'records': [{'id': int(r['id']), 'title': r['title'], 'owner': r['owner'], 'amount': str(r['amount'])} for r in out], 'exported_by': user.get('name')})\n"
s='import json\n'+s
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-800:])
import ctxhelper
req=open('/task/fixtures/stage-3/REQUIREMENTS.md').read()
print(ctxhelper.update(req,{'n.s3':"Stage3 done: output json.dumps({'records':[{id int,title,owner,amount str}] asc id, 'exported_by': user['name']}) (stage2 obligation fulfilled). CSV format replaced (historical: stage1 CSV header id,title,owner,amount)."}))
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in ('n.s1','n.s2','n.s3')]
json.dump(c,open('/task/workspace/context.json','w'))
print([e['id'] for e in c['entries']])