p='/task/workspace/invoice/core.py'
s=open(p).read()
import re
i=s.find('def discount_rate');j=s.find('\ndef ',i+1)
print(s[i:j])
i=s.find('def format_money');print(s[i:])