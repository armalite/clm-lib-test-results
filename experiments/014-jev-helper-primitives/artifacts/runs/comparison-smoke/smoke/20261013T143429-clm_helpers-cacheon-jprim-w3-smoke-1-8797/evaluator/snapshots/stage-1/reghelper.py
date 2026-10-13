import json, clm_jev
P='/task/workspace/context.json'
def load(): return json.load(open(P))
def save(c): json.dump(c,open(P,'w'))
def affected(reg, new_items):
    """reg: {id:text}; new_items: {id:text}. returns {newid:{regid:prob}}"""
    res={}
    for nid,nt in new_items.items():
        r=clm_jev.judge('Does the new change notice item modify, replace or withdraw this existing requirement?', reg, background='New item: '+nt)
        res[nid]=r.get('answers',{}) if r.get('status')=='ok' else {}
    return res
def set_register(c, lines):
    c['entries']=[e for e in c['entries'] if e['id']!='register']
    c['entries'].insert(0,{'id':'register','role':'note','body':'\n'.join(lines)})
