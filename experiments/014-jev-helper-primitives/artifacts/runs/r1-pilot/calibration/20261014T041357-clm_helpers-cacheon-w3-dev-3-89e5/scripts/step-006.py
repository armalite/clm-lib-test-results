import json,subprocess,sys,re
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("if role != 'admin' and r.get('project') not in user.get('projects', []):","if role != 'admin' and r.get('project') not in user.get('projects', []) and r.get('owner') != user.get('name'):")
i=s.index('    buf = io.StringIO()')
s=s[:i]+"""    recs = []
    for r in out:
        t = r['title']
        recs.append({'id': int(r['id']), 'title': t.strip() if isinstance(t, str) else t, 'owner': r['owner'], 'amount': r['amount']})
    doc = {'records': recs, 'exported_by': user.get('name')}
    return json.dumps(doc)
"""
s='import json\n'+s
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
reg=c['entries'][0]['body']
reg=reg.replace("CURRENT [S1.1] Format: CSV via csv.writer default dialect, lineterminator \\n; header id,title,owner,amount; rows ascending id; no records -> header only.","HISTORY [S1.1] Format was CSV (header id,title,owner,amount) - replaced by S3.1.\nCURRENT [S1.1, S3.1] Output: json.dumps object, key 'records' = list ascending id, each exactly keys id(int),title,owner,amount(str as given); no records -> empty list.")
reg=reg.replace("CURRENT [S1.3] admin: any project; others only records with project in user projects (silently skip).","CURRENT [S1.3, S3.2] admin: any project; others (non-viewer) only records with project in user projects OR owner==user['name'] (others silently skipped).")
reg=reg.replace("CURRENT [S2.4] Obligation: if format changes from CSV,","CURRENT [S2.4] Obligation (now triggered by S3.1, applies): if format changes from CSV,")
reg+="\nHISTORY [S3.3] Note: archived storage moves to cheaper tier; no export change."
c['entries']=[{'id':'register','role':'summary','body':reg},{'id':'progress','role':'note','body':'Stages 1-3 implemented in exporter/core.py (JSON output incl exported_by).'}]
json.dump(c,open('/task/workspace/context.json','w'))