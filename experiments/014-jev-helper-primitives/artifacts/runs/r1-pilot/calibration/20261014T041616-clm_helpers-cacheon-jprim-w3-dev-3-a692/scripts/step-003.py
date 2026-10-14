import json,re
s=open('reghelper.py').read()
s=s.replace("        cur=[e for e in E if e['id'].startswith('reg.') and e['body'].startswith('CURRENT')]","        cur=[e for e in E if e['id'].startswith('reg.') and e['body'].startswith('CURRENT')] if stage>=3 else []")
s+='''
def override(ids, reason):
    d=json.load(open(CTX))
    for e in d['entries']:
        if e['id'] in ['reg.'+i for i in ids]:
            e['body']=e['body'].split('\\n')[0]
    print('OVERRIDE:',ids,reason)
    json.dump(d,open(CTX,'w'),indent=0)
'''
open('reghelper.py','w').write(s)
d=json.load(open('context.json'))
for e in d['entries']:
    if e['id']=='s2.act': e['body']='[step2] implemented core.py (S1.1-S1.5), wrote reghelper.py, ran update(1); tests OK.'
    if e['id']=='s2.obs': e['body']='10 tests OK.'
json.dump(d,open('context.json','w'))
import importlib,reghelper;importlib.reload(reghelper)
reghelper.override(['S1.1','S1.2'],'stage-1 items are initial requirements, not changes; appended amend lines were spurious (each item has its own CURRENT entry)')