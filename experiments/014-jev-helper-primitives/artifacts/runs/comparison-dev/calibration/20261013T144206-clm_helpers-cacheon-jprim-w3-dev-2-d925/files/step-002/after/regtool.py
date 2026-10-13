import json, clm_jev
P='/task/workspace/context.json'
def load(): return json.load(open(P))
def save(c): json.dump(c,open(P,'w'))
def affected(new_items, register):
    """new_items: {id:text}; register: {regid:text}. returns {newid:{regid:prob}}"""
    res={}
    for nid,t in new_items.items():
        r=clm_jev.judge('Does this change notice modify, replace or withdraw the given register requirement? Notice: '+t, register)
        res[nid]=r.get('answers',{}) if r.get('status')=='ok' else {}
    return res
def set_entry(c,eid,body,role='summary'):
    c['entries']=[e for e in c['entries'] if e['id']!=eid]+[{'id':eid,'role':role,'body':body}]
