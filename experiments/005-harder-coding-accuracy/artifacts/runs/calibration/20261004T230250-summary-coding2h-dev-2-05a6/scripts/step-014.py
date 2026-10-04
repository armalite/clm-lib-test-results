p='/task/workspace/invoice/core.py'
s=open(p).read()
import re
print(re.findall(r'TIER.*',s)[:2]); print([l for l in s.splitlines() if '0.10' in l or 'tax' in l])