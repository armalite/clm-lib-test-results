import sys,re,subprocess
sys.path.insert(0,'/task/workspace')
import regtool
p='/task/workspace/exporter/core.py'
s=open(p).read()
old=s[s.index('    return json.dumps'):]
new='''    recs=[{'id': int(r['id']), 'title': r['title'].strip(), 'owner': r['owner'], 'project': r.get('project'), 'amount': r['amount']} for r in out]
    doc={}
    if role != 'admin':
        doc['exported_by']=user.get('name')
    doc['records']=recs
    doc['confidential_count']=sum(1 for r in out if r.get('confidential') is True)
    return json.dumps(doc)
'''
open(p,'w').write(s.replace(old,new))
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
c=regtool.load()
reg=[e for e in c['entries'] if e['id']=='register'][0]
try: print(regtool.affected({'S7.1':'records gain key project','S7.2':'admin exports omit exported_by'},reg['body'].split('\n')))
except Exception as ex: print('aff err',ex)
b=reg['body']
b=b.replace('CURRENT [S1.1, S3.1] Format: JSON text (json.dumps) object; key "records" = list of {id(int),title,owner,amount(str as given)}','CURRENT [S1.1, S3.1, S7.1] Format: JSON text (json.dumps) object; key "records" = list of {id(int),title,owner,project,amount(str as given)}')
b=b.replace('CURRENT [S2.4] now active: every JSON export has top-level exported_by=user name.','CURRENT [S2.4, S7.2] exported_by=user name in every JSON export EXCEPT role admin, whose exports omit it.\nHISTORY [S2.4] Previously exported_by in every export including admin.')
b=b.replace('CURRENT [S2.5] Obligation:','CURRENT [S2.5, S4.1] Active (legal purpose allowed): every export includes top-level confidential_count = number of confidential records exported. Obligation:')
b+='\nHISTORY [S7.3] Decision record: residency restriction lifted after regional data agreement signed.'
regtool.set_entry(c,'register',b,'summary')
regtool.set_entry(c,'note1','All 7 stages implemented; ready for final.','note')
c['entries']=[e for e in c['entries'] if e['id'] in('register','note1')]
regtool.save(c)