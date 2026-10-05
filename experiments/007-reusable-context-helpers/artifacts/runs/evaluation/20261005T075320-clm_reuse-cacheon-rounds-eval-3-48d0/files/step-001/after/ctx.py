import json
P='/task/workspace/context.json'
def load():
    try: return json.load(open(P))
    except Exception: return {"format":"clm-context/v1","entries":[]}
def save(d): json.dump(d,open(P,'w'))
def setnote(i,body):
    d=load(); d['entries']=[e for e in d['entries'] if e['id']!=i]; d['entries'].insert(0,{'id':i,'role':'note','body':body}); save(d)
def keep_only(ids):
    d=load(); d['entries']=[e for e in d['entries'] if e['id'] in ids]; save(d)
