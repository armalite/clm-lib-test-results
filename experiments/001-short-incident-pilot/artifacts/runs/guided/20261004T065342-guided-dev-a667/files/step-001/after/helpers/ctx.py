import json
P='/task/workspace/context.json'
def load():
    try: return json.load(open(P))
    except Exception: return {"format":"clm-context/v1","entries":[]}
def compact(note, keep_last=0):
    d=load(); e=d['entries']
    kept=e[-keep_last:] if keep_last else []
    d['entries']=[{"id":"notes","role":"note","body":note}]+[x for x in kept if x['id']!='notes']
    json.dump(d,open(P,'w'))
