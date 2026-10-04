import subprocess,sys,re
p='/task/workspace/invoice/core.py'
s=open(p).read()
i=s.find('def _tax_rate');print(s[i:i+300]);i=s.find('def format_money');print(s[i:i+300])
