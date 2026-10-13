import json
P="/task/workspace/context.json"
def setnotes(text):
    json.dump({"format":"clm-context/v1","entries":[{"id":"notes","role":"note","body":text}]},open(P,"w"))
