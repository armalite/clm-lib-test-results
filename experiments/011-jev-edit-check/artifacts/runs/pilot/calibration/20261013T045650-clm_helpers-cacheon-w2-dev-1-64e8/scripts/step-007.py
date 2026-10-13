import json,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
i=s.index('    buf = io.StringIO()')
s=s[:i]+"    return json.dumps({'exported_by': user.get('name'), 'records': [{'id': int(r['id']), 'title': r['title'], 'owner': r['owner'], 'amount': r['amount']} for r in out]})\n"
s=s.replace('import csv, io','import csv, io, json')
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-800:])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2')]+[{'id':'n3','role':'note','body':'Stage3 done: output now json.dumps({exported_by:user[name], records:[{id int,title,owner,amount str}]}) asc id (replaces CSV). core.py ends with that return.'}]
json.dump(c,open('/task/workspace/context.json','w'))