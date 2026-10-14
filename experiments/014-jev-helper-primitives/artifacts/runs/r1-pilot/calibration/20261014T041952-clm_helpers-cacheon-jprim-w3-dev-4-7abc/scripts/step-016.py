import re
s=open('/task/workspace/exporter/core.py').read()
for i,l in enumerate(s.splitlines(),1):print(i,l)