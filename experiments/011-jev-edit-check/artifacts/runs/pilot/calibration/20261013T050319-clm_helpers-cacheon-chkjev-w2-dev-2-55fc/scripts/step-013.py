import json
c=json.load(open('/task/workspace/context.json'))
e=c['entries']
keep=[x for x in e if x['id'] in('sum1','sum2')]
for x in keep:
    if x['id']=='sum2': x['body']=x['body'].replace(' Next: advance to stage 3.','')
keep.append({'id':'sum3','role':'summary','body':"Stage 3 rules: [NEW Date filter] params may contain 'since' (YYYY-MM-DD); when present only records with created >= since exported. [CHANGED Format] replaces whole stage 1 CSV rule: return json.dumps of object with key \"records\" = list, one object per exported record, ascending id, each exactly keys id(int),title,owner,amount(str exactly as given); tests parse JSON, compare values. Which records exported unchanged. Stage 2 compliance obligation now active: top-level \"exported_by\"=user['name'] included. Implemented in core.py (since filter in loop; json.dumps({'exported_by':..,'records':[...]})); stage 3 visible tests 4/4 OK. Next: advance to stage 4."})
c['entries']=keep
json.dump(c,open('/task/workspace/context.json','w'))
print('ok')