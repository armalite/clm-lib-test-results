import re
b='/task/fixtures/round-09/'
for f in ['board.md','changes.md']:
  for i,l in enumerate(open(b+f),1):print(f,i,l.rstrip())
for i,l in enumerate(open(b+'logs/search-api.log'),1):
  if re.search(r'ERROR|WARN',l) and 'slow' not in l.lower():print(i,l.rstrip()[:150])