s=open('/task/workspace/invoice/core.py').read()
for i,l in enumerate(s.splitlines()):
    if 'tax' in l or 'format' in l or 'abs' in l or 'return' in l: print(i,l)