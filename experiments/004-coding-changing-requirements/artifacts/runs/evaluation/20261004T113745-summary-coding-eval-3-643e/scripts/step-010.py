p='/task/workspace/invoice/core.py';s=open(p).read()
import re
s=s.replace("    if l['qty'] >= 100:\n        a = a * Decimal('0.90')\n","    if l['qty'] >= 200:\n        a = a * Decimal('0.88')\n    elif l['qty'] >= 50:\n        a = a * Decimal('0.95')\n")
open(p,'w').write(s)
print(s)