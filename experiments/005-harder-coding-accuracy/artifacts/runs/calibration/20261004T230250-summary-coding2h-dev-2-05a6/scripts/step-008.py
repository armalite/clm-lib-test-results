p='/task/workspace/invoice/core.py'
s=open(p).read()
import re
print([l for l in s.splitlines() if 'discount' in l or 'amounts' in l])