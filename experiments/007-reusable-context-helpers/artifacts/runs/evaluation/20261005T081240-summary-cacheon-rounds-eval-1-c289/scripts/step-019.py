import json,glob,os
open('/task/workspace/notes.md','a').write('\nR6: logs are JSON now. Board Thread B adds search-api; no other change.\n')
for f in sorted(glob.glob('/task/fixtures/round-06/logs/*.log')):
  for i,l in enumerate(open(f),1):
    try: d=json.loads(l)
    except: print(os.path.basename(f),i,l[:120]);continue
    if d.get('level')!='INFO' and 'slow query' not in d.get('msg',''): print(os.path.basename(f),i,d.get('level'),d.get('msg'),{k:v for k,v in d.items() if k not in('ts','level','svc','msg')})
print(os.path.exists('/task/fixtures/round-06/changes.md'))