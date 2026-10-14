import json, re, clm_jev
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
        cur=[e for e in E if e['id'].startswith('reg.') and e['body'].startswith('CURRENT')] if stage>=3 else []
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

def override(ids, reason):
    d=json.load(open(CTX))
    for e in d['entries']:
        if e['id'] in ['reg.'+i for i in ids]:
            e['body']=e['body'].split('\n')[0]
    print('OVERRIDE:',ids,reason)
    json.dump(d,open(CTX,'w'),indent=0)
