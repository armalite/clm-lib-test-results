import json
P='/task/workspace/context.json'
def load():
    try: return json.load(open(P))
    except Exception: return {"format":"clm-context/v1","entries":[]}
def save(d): json.dump(d,open(P,'w'))
def keep_notes(note_id, body):
    d=load(); e=[x for x in d['entries'] if x['role']=='note' and x['id']!=note_id]
    e.append({'id':note_id,'role':'note','body':body}); d['entries']=e; save(d)
