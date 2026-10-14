import sys;sys.path.insert(0,'/task/workspace')
import regmaint
regmaint.update(4)
import re
s=open('/task/workspace/exporter/core.py').read()
for i,l in enumerate(s.splitlines(),1):print(i,l)