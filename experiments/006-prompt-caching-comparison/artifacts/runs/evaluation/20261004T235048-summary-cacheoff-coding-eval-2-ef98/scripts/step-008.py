s=open('/task/workspace/invoice/core.py').read()
for i,l in enumerate(s.splitlines()):
  if 'tax' in l or 'def format_money' in l or 'PFX' in l or 'return' in l: print(i,l)