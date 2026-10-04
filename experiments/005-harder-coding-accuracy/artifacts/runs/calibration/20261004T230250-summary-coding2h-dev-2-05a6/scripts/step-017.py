p='/task/workspace/invoice/core.py'
s=open(p).read()
for i,l in enumerate(s.splitlines()):
    if 'discount' in l or 'shipping' in l: print(i,l)