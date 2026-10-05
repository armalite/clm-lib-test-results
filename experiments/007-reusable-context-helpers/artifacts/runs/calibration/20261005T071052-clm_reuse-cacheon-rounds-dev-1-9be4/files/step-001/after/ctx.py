import json
P='/task/workspace/context.json'
def load():
    try: return json.load(open(P))
    except Exception: return {"format":"clm-context/v1","entries":[]}
def save(d): json.dump(d,open(P,'w'))
def keep_notes(note_id, body):
    d=load(); d['entries']=[e for e in d['entries'] if e['role']=='note' and e['id']!=note_id]
    d['entries'].append({'id':note_id,'role':'note','body':body}); save(d)
