for f in ['board.md','changes.md']:
  for i,l in enumerate(open('/task/fixtures/round-10/'+f),1): print(f,i,l.rstrip()[:200])
import re
for s in ['search-api','shipping-svc','notify-worker']:
  n=0
  for i,x in enumerate(open('/task/fixtures/round-10/logs/%s.log'%s),1):
    if re.search('config|ERROR|WARN|disk',x,re.I):
      print(s,i,x[:140].rstrip());n+=1
      if n>3:break