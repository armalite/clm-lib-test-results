import json
d=json.load(open('context.json'))
drop={'s1.act','s1.obs','s2.act','s2.obs','s7.obs','s9.act','s9.obs','s11.act','s11.obs','s11.rcpt','s12.act','s12.obs','s13.act','s13.obs','s14.act','s14.obs','s14.rcpt','s5.note'}
d['entries']=[e for e in d['entries'] if e['id'] not in drop]
d['entries'].insert(0,{'id':'st.note','role':'note','body':'Status: stages 1-4 done. core.py implements S1-S4 (JSON+exported_by, owner scope, admin-only include_archived, case-insensitive region, whitespace-collapsed titles); tests OK. reghelper.update(stage) Jev-based ran for 1,3,4; override(ids,reason) prints OVERRIDE. Next: advance to stage 5.'})
json.dump(d,open('context.json','w'))
print(len(d['entries']))