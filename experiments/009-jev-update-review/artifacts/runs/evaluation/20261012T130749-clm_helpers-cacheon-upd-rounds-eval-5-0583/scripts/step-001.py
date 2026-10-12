import os
for r,d,f in os.walk('/task/fixtures'):print(r,f)
print(open('/task/fixtures/round-01/board.md').read()[:2000])
p='/task/fixtures/round-01/changes.md'
if os.path.exists(p):print(open(p).read()[:1500])