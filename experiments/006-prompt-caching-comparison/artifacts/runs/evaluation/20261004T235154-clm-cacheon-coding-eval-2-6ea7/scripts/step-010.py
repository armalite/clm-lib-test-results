import re
s=open('/task/workspace/invoice/core.py').read()
i=s.find('def compute_invoice');print(s[i:])