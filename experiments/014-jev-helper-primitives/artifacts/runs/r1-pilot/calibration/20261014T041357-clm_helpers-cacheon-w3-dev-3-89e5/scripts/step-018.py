import re
p='/task/workspace/exporter/core.py'
s=open(p).read()
for i,l in enumerate(s.splitlines(),1):
    if re.search(r"region|'amount'|\"amount\"",l): print(i,l)
