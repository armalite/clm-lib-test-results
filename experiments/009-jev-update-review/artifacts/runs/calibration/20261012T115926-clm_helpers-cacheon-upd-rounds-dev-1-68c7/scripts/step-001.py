import os
b='/task/fixtures/round-01/'
for r,d,f in os.walk(b):
  for x in f: print(os.path.join(r,x))
print(open(b+'board.md').read()[:1500])
try: print(open(b+'changes.md').read()[:1000])
except Exception as e: print(e)