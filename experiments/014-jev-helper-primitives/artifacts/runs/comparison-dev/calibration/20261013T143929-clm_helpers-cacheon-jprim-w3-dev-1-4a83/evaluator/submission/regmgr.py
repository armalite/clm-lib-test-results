import json, clm_jev
P='/task/workspace/context.json'
def load(): return json.load(open(P))
def save(c): json.dump(c,open(P,'w'),indent=0)
def reg(c): return [e for e in c['entries'] if e['id'].startswith('reg.')]
def affected(new_text, c, thr=0.5):
    items={e['id']:e['body'] for e in reg(c) if e['body'].startswith('CURRENT')}
    if not items: return {}
    r=clm_jev.judge('Does the NEW change item modify, replace, conflict with or withdraw any part of this requirement?',items,background='NEW: '+new_text)
    a=r.get('answers') or {}
    return {k:v for k,v in a.items() if v is not None and v>=thr}
def apply(c, new_items, amendments):
    """new_items: list of (regid, body). amendments: regid -> new CURRENT body or 'HISTORY ...' text.
    Uses jev to flag affected items; prints flagged ones lacking an amendment."""
    for rid,body in new_items:
        if body.startswith('CURRENT') and '[S' in body and rid not in amendments:
            hits=affected(body,c)
            for k,p in hits.items():
                if k not in amendments: print('JEV FLAG',rid,'->',k,round(p,2))
    ents={e['id']:e for e in c['entries']}
    for k,b in amendments.items():
        if k in ents: ents[k]['body']=b
        else: c['entries'].append({'id':k,'role':'summary','body':b})
    for rid,body in new_items:
        if rid in ents: ents[rid]['body']=body
        else: c['entries'].append({'id':rid,'role':'summary','body':body})
    save(c)
