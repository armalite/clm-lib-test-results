import json
P='/task/workspace/context.json'
def load():
    try: return json.load(open(P))
    except Exception: return {"format":"clm-context/v1","entries":[]}
def save(d): json.dump(d,open(P,'w'))
def keep_notes(note):
    d=load(); d['entries']=[e for e in d['entries'] if e['role']=='note']
    d['entries']=[e for e in d['entries'] if e['id']!='notes']+[{"id":"notes","role":"note","body":note}]
    save(d)
