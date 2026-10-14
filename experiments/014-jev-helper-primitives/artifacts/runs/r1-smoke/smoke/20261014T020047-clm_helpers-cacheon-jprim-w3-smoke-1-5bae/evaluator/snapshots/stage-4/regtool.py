import re, json
import clm_jev
CTX='/task/workspace/context.json'
Q=("Does the NEW requirement change, replace, restrict, extend or withdraw any part of the EXISTING register item "
   "(i.e. they govern the same behaviour and the new one alters it)?")
def parse(stage):
    t=open(f'/task/fixtures/stage-{stage}/REQUIREMENTS.md').read()
    items=re.findall(r'^- \[(S\d+\.\d+)\]\s*(.+?)(?=^- \[|^#|^Visible|\Z)', t, re.S|re.M)
    notes=set(re.findall(r'\[(S\d+\.\d+)\]\s*(?:Decision record|Note|Information)', t))
    sec=t.split('## Notes')[1] if '## Notes' in t else ''
    notes|=set(re.findall(r'\[(S\d+\.\d+)\]', sec))
    return [(i,' '.join(x.split())) for i,x in items], notes
def update(stage, thr=0.6, info=None):
    info=info or {}
    c=json.load(open(CTX)); E=c['entries']
    items,notes=parse(stage)
    for iid,txt in items:
        if iid in notes:
            E.append({'id':'reg.'+iid,'role':'note','body':f'HISTORY [{iid}] note/decision: {txt}'}); continue
        cur=[e for e in E if e['id'].startswith('reg.') and e['body'].startswith('CURRENT')]
        hit=[]
        if cur:
            r=clm_jev.judge(Q,{e['id']:e['body'][:1500] for e in cur[:20]},background='NEW requirement: '+txt+' '+info.get(iid,''))
            if r.get('status')!='ok': print('FALLBACK:',iid,'jev error'); r={'answers':{}}
            hit=[e for e in cur if (r['answers'].get(e['id']) or 0)>=thr]
        for e in hit:
            ids=re.search(r'\[([^\]]*)\]',e['body']).group(1)
            E.append({'id':e['id']+'.h'+iid,'role':'note','body':'HISTORY '+e['body'][8:]+f' (superseded in part by {iid})'})
            e['body']=f'CURRENT [{ids}, {iid}] '+e['body'][len(ids)+11:]+f' || AMENDED by {iid} (wins on conflict; rest stays): {txt}'
        if not hit:
            E.append({'id':'reg.'+iid,'role':'note','body':f'CURRENT [{iid}] {txt}'})
        print(iid,'->',[e['id'] for e in hit])
    json.dump(c,open(CTX,'w'))
def override(eid, body, reason):
    c=json.load(open(CTX))
    for e in c['entries']:
        if e['id']==eid: e['body']=body
    print('OVERRIDE:',eid,reason); json.dump(c,open(CTX,'w'))
