import subprocess,sys,json
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace("if str(r.get('region') or '').lower() == 'ch' and 'ch' not in regions:","if False:")
s=s.replace("'amount': r['amount']})","'amount': r['amount'], 'project': r.get('project')})")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
cp='/task/workspace/context.json'
c=json.load(open(cp))
for e in c['entries']:
    if e['id']=='register':
        b=e['body']
        b=b.replace("CURRENT [S3.1, S1.1] Output: json.dumps object with 'records': list of {id,title,owner,amount} (exactly these keys)","CURRENT [S3.1, S1.1, S7.1] Output: json.dumps object with 'records': list of {id,title,owner,amount,project} (exactly these keys; project added by S7.1)")
        b=b.replace("CURRENT [S2.2, S4.2] region 'ch' exported only if 'ch' in user['regions'], admins too; region compare case-insensitive (records and user regions).","HISTORY [S2.2, S4.2] region 'ch' formerly exported only if 'ch' in user['regions'] (case-insensitive) - withdrawn by S7.2.\nCURRENT [S7.2] No residency restriction: records of every region exported under ordinary rules.")
        b+="\nHISTORY [S7.3] Note: stage 7 does not change confidential-record rules."
        e['body']=b
    if e['id']=='status': e['body']='Stages 1-7 implemented in exporter/core.py.'
c['entries']=[e for e in c['entries'] if e['id'] in('register','status')]
json.dump(c,open(cp,'w'))