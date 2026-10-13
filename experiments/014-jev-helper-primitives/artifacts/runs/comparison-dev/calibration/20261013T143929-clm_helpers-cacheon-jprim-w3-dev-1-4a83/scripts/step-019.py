import re
s=open('/task/workspace/exporter/core.py').read()
for i,l in enumerate(s.split('\n'),1):
    if re.search(r"region|'amount'|\"amount\"",l): print(i,l)
print(open('/task/workspace/regmgr.py').read()[:1500])