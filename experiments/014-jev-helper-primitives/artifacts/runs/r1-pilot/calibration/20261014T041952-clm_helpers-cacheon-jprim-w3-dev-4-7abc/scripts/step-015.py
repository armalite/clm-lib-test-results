import sys;sys.path.insert(0,'/task/workspace')
import regmaint
regmaint.update(5)
import json;c=regmaint.load()
for e in c['entries']:
  if e['id'].startswith('reg.'):print(e['id'],e['body'][:160])