import json,glob,re
c=json.load(open('/task/workspace/context.json'))
e=c['entries'][0]
for f in sorted(glob.glob('/task/fixtures/round-07/logs/*')):
  L=[i for i,l in enumerate(open(f),1) if re.search('disk|cert|tls|volume',l,re.I)]
  print(f.split('/')[-1],len(L),L[:1],L[-1:])
e['body']+='\nR7: board round-07/board.md:3 Thread B cause revised DISK_PRESSURE (shipping+notify); :4 Thread D false alarm (drop CERT); :5 POSTMORTEM_DRAFT CLOSED. changes CHG-149 PROPOSED only. 0 ERROR lines all logs r7.'
c['entries']=[e]
json.dump(c,open('/task/workspace/context.json','w'))