import json,subprocess,sys
p='/task/workspace/exporter/core.py'
s=open(p).read()
s=s.replace('import csv, io','import json')
s=s.replace('r["created"] < since','(r.get("updated") or r["created"]) < since')
i=s.index('    buf = io.StringIO()')
s=s[:i]+'''    recs = [{"id": r["id"], "title": r["title"].strip(), "owner": r["owner"], "amount": r["amount"]} for r in out]
    return json.dumps({"exported_by": user.get("name"), "records": recs})
'''
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c=json.load(open('/task/workspace/context.json'))
reg=c['entries'][0]['body']
reg=reg.replace("CURRENT [S1.1] Format: CSV","HISTORY [S1.1] Format was CSV")
reg=reg.replace("CURRENT [S1.4] Date filter: params 'since' YYYY-MM-DD -> only records with created >= since.","HISTORY [S1.4] Date filter originally on created.\nCURRENT [S1.4, S3.2] params 'since' YYYY-MM-DD -> only records whose date >= since; date = 'updated' if record has one, else 'created'.")
reg=reg.replace("CURRENT [S2.4] Obligation:","CURRENT [S2.4, S3.1] Obligation now active (format is JSON): top-level exported_by=user['name'] in every export. Orig:")
reg+='''\nCURRENT [S1.1, S3.1] Format: json.dumps object with key "records": list of {id(int),title,owner,amount(str exactly as given)} ascending id; no records -> empty list. Plus exported_by.\nHISTORY [S3.3] Note: web UI shows owner display name; exports keep stored owner.'''
c['entries']=[{'id':'register','role':'summary','body':reg},{'id':'note1','role':'note','body':'Stages 1-3 implemented in exporter/core.py (filter loop + json output). Next: advance.'}]
json.dump(c,open('/task/workspace/context.json','w'))