import re
p='/task/workspace/invoice/core.py';c=open(p).read()
for i,l in enumerate(c.splitlines(),1):
    if 'def ' in l or 'tax' in l or 'format_money' in l: print(i,l)
print(open('/task/workspace/invoice/__init__.py').read())