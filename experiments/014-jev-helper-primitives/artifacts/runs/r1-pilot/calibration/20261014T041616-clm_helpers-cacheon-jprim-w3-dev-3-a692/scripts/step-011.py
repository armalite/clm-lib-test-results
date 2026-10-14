import reghelper,json
reghelper.override(['S2.4'],'S3.1 changes format (S1.1), not the exported_by obligation; S2.4 now applies and stays in force unchanged')
d=json.load(open('context.json'))
for e in d['entries']:
    if e['id']=='s9.act': e['body']='[step9] implemented S3 in core (JSON+exported_by, owner scope), ran update(3); tests OK.'
    if e['id']=='s9.obs': e['body']='Jev: S3.1->S1.1 retired (0.98); S3.2->S1.3 amended (0.94); S3.1 also wrongly amended S2.4 (0.85). 4 tests OK.'
d['entries']=[e for e in d['entries'] if e['id'] not in ('s10.act','s10.obs','s2.rcpt','s9.rcpt')]
json.dump(d,open('context.json','w'))
print([e['body'][:80] for e in d['entries'] if e['id']=='reg.S2.4'])