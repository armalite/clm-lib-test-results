print(open('/task/fixtures/round-09/board.md').read())
import re
for l in ['search-api','shipping-svc','notify-worker']:
  for i,x in enumerate(open(f'/task/fixtures/round-09/logs/{l}.log'),1):
    if re.search('ERROR|WARN|config|disk',x): print(l,i,x[:150].rstrip())