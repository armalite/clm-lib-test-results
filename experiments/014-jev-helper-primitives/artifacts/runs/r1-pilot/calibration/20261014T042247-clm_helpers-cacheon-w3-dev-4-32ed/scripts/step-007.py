p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("r.get('created', '') < since","(r.get('updated') or r.get('created', '')) < since")
i=s.index('    buf = io.StringIO()')
s=s[:i]+'''    import json
    obj = {'records': [{'id': r['id'], 'title': str(r['title']).strip(), 'owner': r['owner'], 'amount': r['amount']} for r in out], 'exported_by': user.get('name')}
    cc = sum(1 for r in out if r.get('confidential') is True)
    if cc and params.get('purpose') != 'audit':
        obj['confidential_count'] = cc
    return json.dumps(obj)
'''
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
reg=c['entries'][0]
b=reg['body'].replace('CURRENT [S1.1] Format: CSV','HISTORY [S1.1] Format was CSV').replace("CURRENT [S1.4] params 'since' YYYY-MM-DD: only created >= since.","HISTORY [S1.4] since compared created only.\nCURRENT [S1.4, S3.2] params 'since' YYYY-MM-DD: only records whose updated (if present) else created >= since.")
b+="\nCURRENT [S3.1, S1.1, S1.5, S2.4] Format: json.dumps object {'records':[{id int,title stripped,owner,amount str exact}] asc id, 'exported_by': user['name']}; no records -> empty list.\nCURRENT [S2.5] confidential_count added when confidential exported and purpose!='audit' (implemented).\nHISTORY [S3.3] Note: web UI shows owner display names; exports keep stored owner."
reg['body']=b
c['entries']=[reg,{'id':'prog','role':'note','body':'Stages 1-3 implemented in exporter/core.py (JSON output).'}]
json.dump(c,open('/task/workspace/context.json','w'))