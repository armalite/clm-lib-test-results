import json,glob,re
note=open('/task/workspace/context.json').read()
c=json.loads(note)
c['entries']=[e for e in c['entries'] if e['id']=='n1']
c['entries'][0]['body']=c['entries'][0]['body'].replace('Q6: TODO.','Q6: HB-22 §2 facilities 10500 (cite HB-15 §2, HB-22 §2).')
json.dump(c,open('/task/workspace/context.json','w'))
for p in glob.glob('/task/workspace/search-results/*SR-008*')+[x for x in glob.glob('/task/workspace/search-results/*') if 'SR-008' in open(x).read()[:300]][:1]:
  for l in open(p):
    if l.startswith('---') or re.search(r'\d',l): print(l.strip()[:220])
  break