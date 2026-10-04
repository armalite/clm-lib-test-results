import re
s=open('/task/workspace/invoice/core.py').read()
for i,l in enumerate(s.split('\n'),1):
    if re.search(r'tax|def format_money|PREFIX|quantize|return|f\'|format',l): print(i,l)