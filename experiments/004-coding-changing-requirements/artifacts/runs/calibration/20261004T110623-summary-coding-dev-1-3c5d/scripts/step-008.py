import re
p='/task/workspace/invoice/core.py'
s=open(p).read()
i=s.find('def discount_rate');print(s[i:i+400])
i=s.find('def format_money');print(s[i:i+300])