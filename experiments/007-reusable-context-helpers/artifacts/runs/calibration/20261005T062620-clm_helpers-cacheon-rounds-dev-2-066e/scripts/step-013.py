import sys
sys.path.insert(0,'/task/workspace')
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-05/'+f),1):print(f,i,l.rstrip())
from h import scan
scan(5)