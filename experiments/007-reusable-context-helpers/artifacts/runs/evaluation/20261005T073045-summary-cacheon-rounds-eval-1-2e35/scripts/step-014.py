import glob
r=[]
for f in ['search-api','shipping-svc']:
  ls=[i for i,l in enumerate(open(f'/task/fixtures/round-05/logs/{f}.log'),1) if 'certificate_expired' in l]
  r.append(f'{f}:{ls}')
  print(f,ls,[l.rstrip()[:140] for l in open(f'/task/fixtures/round-05/logs/{f}.log') if 'certificate_expired' in l][:1])
open('/task/workspace/notes.md','a').write('\nR5: board.md:3 Thread A mitigated; changes.md:3 CHG-143 APPLIED mitigation payments. lag gone. cert errors now also search-api: '+' '.join(r)+'\n')