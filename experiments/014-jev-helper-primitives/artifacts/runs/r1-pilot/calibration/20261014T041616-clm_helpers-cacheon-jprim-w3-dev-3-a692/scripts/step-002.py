import os,subprocess,sys
os.makedirs('exporter',exist_ok=True)
open('exporter/core.py','w').write('''import csv, io

def export_records(records, user, params):
    params = params or {}
    role = user.get('role')
    if role == 'viewer':
        raise PermissionError('viewer')
    out = []
    for r in sorted(records, key=lambda r: r['id']):
        if role != 'admin' and r['project'] not in user.get('projects', []):
            continue
        if r['status'] != 'active' and not (r['status'] == 'archived' and params.get('include_archived') is True):
            continue
        if r['confidential'] is True and not (role == 'admin' and params.get('purpose') == 'audit'):
            continue
        out.append(r)
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator='\\n')
    w.writerow(['id', 'title', 'owner', 'amount'])
    for r in out:
        w.writerow([r['id'], r['title'], r['owner'], r['amount']])
    return buf.getvalue()
''')
open('reghelper.py','w').write(r'''import json, re, clm_jev
CTX='/task/workspace/context.json'
def parse(stage):
    t=open(f'/task/fixtures/stage-{stage}/REQUIREMENTS.md').read()
    items=[]
    for m in re.finditer(r'^- \[(S\d+\.\d+)\]\s*(.+?)(?=^- \[|^#|\Z)', t, re.S|re.M):
        items.append((m.group(1),' '.join(m.group(2).split())))
    return items
def update(stage, replace_thr=0.7, amend_thr=0.5, notes=None):
    notes=notes or {}
    d=json.load(open(CTX)); E=d['entries']
    for iid,txt in parse(stage):
        isnote=bool(re.match(r'(Decision record|Note|Information)',txt))
        if isnote:
            E.append({'id':'reg.'+iid,'role':'note','body':f'HISTORY [{iid}] {txt}'}); continue
        cur=[e for e in E if e['id'].startswith('reg.') and e['body'].startswith('CURRENT')]
        if cur:
            items={e['id']:e['body'] for e in cur}
            bg='New change item: '+txt+(' Context: '+notes[iid] if iid in notes else '')
            r1=clm_jev.judge('Does the new change item completely replace this existing requirement, so nothing of the existing one remains in force?',items,background=bg)
            r2=clm_jev.judge('Does the new change item conflict with or modify some part of this existing requirement?',items,background=bg)
            if r1.get('status')!='ok' or r2.get('status')!='ok':
                print('FALLBACK:',iid,'jev error')
            else:
                for e in cur:
                    p1=r1['answers'].get(e['id']) or 0; p2=r2['answers'].get(e['id']) or 0
                    if p1>=replace_thr:
                        e['body']='HISTORY (replaced by '+iid+') '+e['body'][8:]
                    elif p2>=amend_thr:
                        e['body']=e['body']+f'\nCURRENT [{iid}] amends the above: where they conflict, this wins: '+txt
                    print(iid,e['id'],round(p1,2),round(p2,2))
        E.append({'id':'reg.'+iid,'role':'note','body':f'CURRENT [{iid}] {txt}'})
    json.dump(d,open(CTX,'w'),indent=0)
''')
import json
d=json.load(open('context.json'))
for e in d['entries']:
    if e['id']=='s1.obs': e['body']='Stage1 read; exporter/core.py implements S1.1-S1.5. reghelper.update(stage) maintains register.'
    if e['id']=='s1.act': e['body']='[step1] read stage 1'
json.dump(d,open('context.json','w'))
import reghelper; reghelper.update(1)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],capture_output=True,text=True);print(r.stderr[-800:])