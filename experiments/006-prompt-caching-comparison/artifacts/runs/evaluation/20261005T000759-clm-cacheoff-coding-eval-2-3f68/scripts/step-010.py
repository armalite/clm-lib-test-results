import re
s=open('/task/workspace/invoice/core.py').read()
for i,l in enumerate(s.split('\n'),1):
    if re.search(r'tax|format|PREFIX|return|def ',l): print(i,l)