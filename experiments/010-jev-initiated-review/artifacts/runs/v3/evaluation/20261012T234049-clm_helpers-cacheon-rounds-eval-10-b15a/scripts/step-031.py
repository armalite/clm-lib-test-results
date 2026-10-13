import re,glob
for f in ['board.md','changes.md']:
 print(f);print(open('/task/fixtures/round-11/'+f).read())
for f in sorted(glob.glob('/task/fixtures/round-11/logs/*')):
 L=[i+1 for i,l in enumerate(open(f)) if re.search('ERROR|FATAL|429|fail',l) and 'slow' not in l]
 print(f.split('/')[-1],len(L),L[:3],L[-3:])
 if L: print(open(f).readlines()[L[0]-1][:200])