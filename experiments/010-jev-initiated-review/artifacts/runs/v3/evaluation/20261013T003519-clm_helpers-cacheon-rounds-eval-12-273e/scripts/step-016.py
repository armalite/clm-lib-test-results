import re
b='/task/fixtures/round-06/'
for f in ['board.md','changes.md']:
 print(f);print(open(b+f).read())
import os
for f in sorted(os.listdir(b+'logs')):
 L=open(b+'logs/'+f).read().splitlines()
 hits=[(i+1,l) for i,l in enumerate(L) if re.search('ERROR|WARN|error|warn',l) and 'slow' not in l]
 print(f,len(hits))
 for i,l in hits[:2]+hits[-1:]: print(i,l[:200])