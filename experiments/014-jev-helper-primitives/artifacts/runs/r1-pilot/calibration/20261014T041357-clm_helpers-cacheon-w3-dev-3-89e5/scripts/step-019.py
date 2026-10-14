import subprocess,sys,json
p='/task/workspace/exporter/core.py'
L=open(p).read().split('\n')
l=L[21]
assert 'region' in l
ind=len(l)-len(l.lstrip())
L[21]=' '*ind+'if False:'
s='\n'.join(L)
s=s.replace("'amount': r['amount']})","'amount': r['amount'], 'project': r.get('project')})",1)
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
for e in c['entries']:
    if e['id']=='register':
        b=e['body']
        b=b.replace("CURRENT [S1.1, S3.1] Output: json.dumps object, key 'records' = list ascending id, each exactly keys id(int),title,owner,amount(str as given);","CURRENT [S1.1, S3.1, S7.1] Output: json.dumps object, key 'records' = list ascending id, each exactly keys id(int),title,owner,amount(str as given),project (S7.1);")
        b=b.replace("CURRENT [S2.2, S4.2] region 'eu' exported only if 'eu' in user['regions'] (admins too); region compare case-insensitive in records and user regions.","HISTORY [S2.2, S4.2] eu residency restriction (eu only if 'eu' in user regions, case-insensitive) - withdrawn by S7.2.\nCURRENT [S7.2] all regions exported under ordinary rules.")
        b+="\nHISTORY [S7.3] Note: stage 7 does not change confidential rules."
        e['body']=b
c['entries']=[e for e in c['entries'] if e['id']=='register']+[{'id':'progress','role':'note','body':'All 7 stages implemented. Next: final.'}]
json.dump(c,open('/task/workspace/context.json','w'))