import json
P='/task/workspace/context.json'
def load():
    try: return json.load(open(P))
    except Exception: return {"format":"clm-context/v1","entries":[]}
def save(d): json.dump(d,open(P,'w'))
def keep_notes(note_body):
    d={"format":"clm-context/v1","entries":[{"id":"notes","role":"note","body":note_body}]}
    save(d)
