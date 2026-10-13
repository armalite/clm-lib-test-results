import json,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("if role != 'admin' and r['project'] not in user.get('projects', []):","if role != 'admin' and r['project'] not in user.get('projects', []) and r.get('owner') != user.get('name'):")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-800:])
c=json.load(open('/task/workspace/context.json'))
c['entries']=[e for e in c['entries'] if e['id'] in('n1','n2','n3')]+[{'id':'n4','role':'note','body':'Stage4 done: non-admin also gets records where owner==user[name] even outside projects (project filter condition in core.py loop). Other filters still apply.'}]
json.dump(c,open('/task/workspace/context.json','w'))