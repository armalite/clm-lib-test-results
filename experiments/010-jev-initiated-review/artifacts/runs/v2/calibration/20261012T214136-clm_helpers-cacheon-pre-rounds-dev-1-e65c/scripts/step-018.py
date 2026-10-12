import re
b='/task/fixtures/round-05/'
print(open(b+'board.md').read());print(open(b+'changes.md').read())
for s in ['auth-svc','checkout-api','notify-worker','payments-svc','search-api']:
  L=open(b+'logs/'+s+'.log').read().splitlines()
  e=[(i+1,l[:110]) for i,l in enumerate(L) if re.search('ERROR|WARN|error|fail|429|exhaust',l)]
  print(s,len(e));[print(x) for x in e[:3]];print('lines',[x[0] for x in e][:30])