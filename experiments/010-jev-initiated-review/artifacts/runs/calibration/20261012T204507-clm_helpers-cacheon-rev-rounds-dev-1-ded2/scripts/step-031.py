r='/task/fixtures/round-10/'
print(open(r+'board.md').read());print(open(r+'changes.md').read())
import re
for s in ['notify-worker','payments-svc','checkout-api','auth-svc','search-api']:
  L=[i for i,l in enumerate(open(r+'logs/'+s+'.log'),1) if re.search('429|max_inflight|validation|pool|ERROR',l)]
  print(s,len(L),L[:8])