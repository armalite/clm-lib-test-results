import sys;sys.path.insert(0,'/task/workspace')
import h
for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-08/'+f),1):print(f,i,l.rstrip())
h.scan(8)