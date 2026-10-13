import json, clm_jev
P='/task/workspace/context.json'
def load(): return json.load(open(P))
def save(c): json.dump(c, open(P,'w'))
def update(new_req, new_notes, drop_prefixes=('s',)):
    """Ask Jev whether new requirements affect each note; keep unaffected/historical, mark affected."""
    c = load(); ents = c['entries']
    notes = {e['id']: e['body'] for e in ents if e['role']=='note'}
    probs = {}
    if notes:
        r = clm_jev.judge('Do the new requirements change or replace the rule described in this note?', notes, background=new_req[:6000])
        if r.get('status')=='ok': probs = r['answers']
    keep = []
    for e in ents:
        if e['role']=='note':
            p = probs.get(e['id'])
            if 'HISTORICAL' not in e['body'] and p is not None and p > 0.5:
                e['body'] = '[REVIEW: possibly affected by newer stage, see CHANGED rules] ' + e['body']
            keep.append(e)
        elif not e['id'].startswith(drop_prefixes):
            keep.append(e)
    for i,b in new_notes.items(): keep.append({'id':i,'role':'note','body':b})
    c['entries'] = keep; save(c); return probs
