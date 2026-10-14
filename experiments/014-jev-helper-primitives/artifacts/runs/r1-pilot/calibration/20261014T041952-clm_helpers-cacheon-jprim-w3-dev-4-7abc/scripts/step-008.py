import sys;sys.path.insert(0,'/task/workspace')
import regmaint
regmaint.update(3)
c=regmaint.load()
for e in c['entries']:
  if e['id'].startswith('reg.'):print(e['id'],e['body'][:90])
print(open('/task/fixtures/current-tests/test_stage.py').read()[:1500])