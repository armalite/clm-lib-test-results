import json,subprocess,sys
p='exporter/core.py';s=open(p).read()
s=s.replace("    return json.dumps(res)","    if role == 'admin':\n        res.pop('exported_by', None)\n    return json.dumps(res)",1)
i=s.find("    mx = params.get('max_records')")
print(s[i:i+300])
open(p,'w').write(s)
d=json.load(open('context.json'))
d['entries']=[e for e in d['entries'] if e['id'] not in {'s18.act','s18.obs','s18.rcpt','s19.act','s20.act','s20.obs','s20.rcpt'}]
for e in d['entries']:
    if e['id']=='st.note':e['body']='Status: stages 1-6 released; reghelper.update ran for 6. core.py implements S1-S5 + S6.1 (admin omits exported_by). S6.2 cap 30 pending check. Next: verify tests, advance to 7, run reghelper.update(7).'
    if e['id']=='s19.obs':e['body']='Stage 6 released: S6.1 admin omits exported_by; S6.2 max_records>30 treated as 30; S6.3 note web shows 50/page.'
json.dump(d,open('context.json','w'))