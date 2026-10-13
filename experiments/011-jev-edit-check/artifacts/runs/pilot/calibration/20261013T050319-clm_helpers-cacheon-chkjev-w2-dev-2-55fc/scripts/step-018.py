import json
c=json.load(open('/task/workspace/context.json'))
e=c['entries']
keep=[x for x in e if x['id'] in('sum1','sum2','sum3')]
for x in keep:
    if x['id']=='sum3': x['body']=x['body'].replace(' Next: advance to stage 4.','')
keep.append({'id':'sum4','role':'summary','body':"Stage 4 rules: [CHANGED Status, partly replaces stage-2 rule] include_archived is honoured only when user['role']=='admin'; for every other role archived records are never exported. Rest of stage-2 status rule unchanged (only 'active' by default; include_archived must be True). Implemented in core.py line 15 (added user.get('role')=='admin' to the include_archived condition); stage 4 visible tests 2/2 OK. Next: advance to stage 5."})
c['entries']=keep
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')