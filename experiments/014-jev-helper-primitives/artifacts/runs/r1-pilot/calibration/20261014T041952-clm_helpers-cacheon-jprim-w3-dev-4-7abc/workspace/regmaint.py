import json,re
CTX="/task/workspace/context.json"
def load():
    return json.load(open(CTX))
def save(c):
    json.dump(c,open(CTX,"w"),indent=0)
def parse(stage):
    t=open(f"/task/fixtures/stage-{stage}/REQUIREMENTS.md").read()
    items=[];note=False
    for line in t.splitlines():
        if line.startswith("## "): note="Note" in line
        m=re.match(r"- \[(S\d+\.\d+)\] (.*)",line)
        if m: items.append((m.group(1),m.group(2),note))
    return items
def regs(c):
    return [e for e in c["entries"] if e["id"].startswith("reg.") and e["body"].startswith("CURRENT")]
def update(stage,thr=0.5,rthr=0.75,extra=None):
    import clm_jev
    c=load();extra=extra or {}
    for iid,text,isnote in parse(stage):
        if isnote:
            c["entries"].append({"id":"reg."+iid,"role":"note","body":f"HISTORY [{iid}] note: {text}"});continue
        cur=regs(c);hits=[]
        if stage>=3 and cur:
            nt=text+(" "+extra[iid] if iid in extra else "")
            for i in range(0,len(cur),20):
                ch=cur[i:i+20]
                r=clm_jev.judge("Does the NEW change item modify, replace, override or withdraw any part of this existing requirement (same topic, conflicting rule)?",{e["id"]:e["body"] for e in ch},background="NEW change item: "+nt)
                if r.get("status")!="ok": print("FALLBACK:",iid,"jev error");continue
                hits+=[e for e in ch if (r["answers"].get(e["id"]) or 0)>thr]
            if hits:
                r=clm_jev.judge("Does the NEW change item completely replace this existing requirement so that NO part of it remains in force?",{e["id"]:e["body"] for e in hits},background="NEW change item: "+nt)
                ans=r["answers"] if r.get("status")=="ok" else {}
                for e in hits:
                    ids=re.search(r"\[(.*?)\]",e["body"]).group(1)
                    if (ans.get(e["id"]) or 0)>rthr:
                        e["body"]="HISTORY"+e["body"][7:]+f" (replaced by {iid})"
                    else:
                        e["body"]=f"CURRENT [{ids}, {iid}]"+e["body"][len(ids)+10:]+f" AMENDED by {iid}: {text}"
                print(iid,"affects",[e["id"] for e in hits])
        if not hits:
            c["entries"].append({"id":"reg."+iid,"role":"note","body":f"CURRENT [{iid}] {text}"})
    save(c)
def override(eid,body,reason):
    c=load()
    for e in c["entries"]:
        if e["id"]==eid: e["body"]=body
    print("OVERRIDE:",eid,reason);save(c)
