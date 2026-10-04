import re
for i,l in enumerate(open('/task/workspace/invoice/core.py').read().splitlines(),1):
    if re.search(r'tax|def |return|\$|:,|f\'',l): print(i,l)