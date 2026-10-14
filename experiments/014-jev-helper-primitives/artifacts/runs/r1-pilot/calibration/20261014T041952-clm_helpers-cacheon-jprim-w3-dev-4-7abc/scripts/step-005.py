import sys;sys.path.insert(0,'/task/workspace')
import regmaint
regmaint.update(2)
print(open('/task/workspace/exporter/core.py').read())