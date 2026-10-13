import json,glob,os
d=json.load(open('/task/workspace/context.json'))
for e in d['entries']:
  if e['id']=='notes': e['body']+="\nR9: board.md:3 Thread C opened shipping-svc pod failures cause unknown ongoing (suspect CHG-113 R1 changes.md:3); :4 FU OPEN RUNBOOK_UPDATE; :5 FU OPEN CUSTOMER_COMMS. scan.py prints INFO now - use own grep for level ERROR/WARN."
d['entries']=[e for e in d['entries'] if e['id']=='notes']
json.dump(d,open('/task/workspace/context.json','w'))
for f in sorted(glob.glob('/task/fixtures/round-09/logs/*.log')):
  L=[(i,l.strip()) for i,l in enumerate(open(f),1) if '"INFO"' not in l and 'INFO' not in l[:40]]
  print(os.path.basename(f),len(L))
  for i,l in L[:3]+L[-1:]: print(i,l[:200])