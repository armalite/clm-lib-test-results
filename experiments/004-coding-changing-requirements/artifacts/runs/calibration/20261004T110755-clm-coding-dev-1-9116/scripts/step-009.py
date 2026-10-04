p='/task/workspace/invoice/core.py'
s=open(p).read()
i=s.index('def discount_rate');print(s[i:i+700])
import re
print([l for l in open('/task/fixtures/current-tests/test_invoice.py') if 'format_money' in l or 'platinum' in l])