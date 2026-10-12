import json,re
d=json.load(open('/task/workspace/context.json'))
d['entries']=[e for e in d['entries'] if e['id']=='n1']
d['entries'][0]['body']+=' R9: board.md:3 Thread A RESOLVED; :4 Thread B cause revised DISK_PRESSURE (checkout+payments); :5 Thread C ledger-svc failures ongoing cause unknown; :6 OPEN VENDOR_TICKET; changes.md:3 CHG-163 irrelevant.'
json.dump(d,open('/task/workspace/context.json','w'))
for i,l in enumerate(open('/task/fixtures/round-09/logs/ledger-svc.log'),1):
  if re.search(r'ERROR|pool|refused|fail',l,re.I): print(i,l.strip()[:160])
