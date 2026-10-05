import json
P='/task/workspace/context.json'
def load():
    try: return json.load(open(P))
    except Exception: return {"format":"clm-context/v1","entries":[]}
def save(d): json.dump(d,open(P,'w'))
def reset(notes):
    save({"format":"clm-context/v1","entries":[{"id":"n%d"%i,"role":"note","body":b} for i,b in enumerate(notes)]})
