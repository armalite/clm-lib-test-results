import re,sys,subprocess,json
sys.path.insert(0,'/task/workspace')
import regtool
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("r.get('created', '') < since","(r.get('updated') or r.get('created', '')) < since")
i=s.find('    buf = io.StringIO()')
s=s[:i]+"    import json\n    return json.dumps({'exported_by': user.get('name'), 'records': [{'id': int(r['id']), 'title': r['title'].strip(), 'owner': r['owner'], 'amount': r['amount']} for r in out]})\n"
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c=regtool.load()
reg=[e for e in c['entries'] if e['id']=='register'][0]['body']
lines=reg.split('\n')
items={str(k):l for k,l in enumerate(lines) if l.startswith('CURRENT')}
new={'S3.1':'Exports are now JSON object with key records listing objects id(int),title,owner,amount(str) ascending id.','S3.2':'Date filter uses updated date when present else created.'}
aff=regtool.affected(new,items);print(aff)
rep={'S1.1':"CURRENT [S1.1, S3.1] Format: JSON text (json.dumps) object; key \"records\" = list of {id(int),title,owner,amount(str as given)} ascending id; no records -> empty list. Plus \"exported_by\" per S2.4.\nHISTORY [S1.1] Was CSV (csv.writer, header id,title,owner,amount), replaced by S3.1.",'S1.4':"CURRENT [S1.4, S3.2] Date filter: params since YYYY-MM-DD -> only records whose date >= since; date = 'updated' if present else 'created'.\nHISTORY [S1.4] Previously used 'created' only."}
out=[]
for k,l in enumerate(lines):
    hit=[n for n in aff if (aff[n].get(str(k)) or 0)>0.5]
    m=re.match(r'CURRENT \[(S1\.[14])\]',l)
    if m: out.append(rep[m.group(1)])
    else:
        if hit: print('flagged but kept:',l[:60],hit)
        out.append(l)
out.append('CURRENT [S2.4] now active: every JSON export has top-level exported_by=user name.\nHISTORY [S3.3] Note: web UI shows owner display names; exports keep stored owner value.')
regtool.set_entry(c,'register','\n'.join(out))
regtool.set_entry(c,'note1','Stages 1-3 implemented in exporter/core.py (JSON output). Helper regtool.py (load,save,affected,set_entry). Next: advance.','note')
c['entries']=[e for e in c['entries'] if e['id'] in('register','note1')]
regtool.save(c)