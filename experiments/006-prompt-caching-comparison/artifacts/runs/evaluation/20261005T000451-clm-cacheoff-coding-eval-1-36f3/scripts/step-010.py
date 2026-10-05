p='/task/workspace/invoice/core.py'
s=open(p).read()
import re
i=s.index('def tax_rate'); j=s.index('\n\n\n',i)
s=s[:i]+"""def tax_rate(customer=None):
    c = customer or {}
    if c.get('tax_exempt') is True:
        return Decimal('0')
    return {'NZ': Decimal('0.15'), 'AU': Decimal('0.10'), 'US': Decimal('0')}.get(c.get('region'), Decimal('0.12'))"""+s[j:]
i=s.index('def format_money')
s=s[:i]+"""def format_money(amount, currency):
    pre = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}.get(currency)
    if pre is None:
        raise ValueError('unknown currency')
    a = Decimal(str(amount)).quantize(Q, rounding=ROUND_HALF_UP)
    sign = '-' if a < 0 else ''
    return sign + pre + str(abs(a))
"""
open(p,'w').write(s)
print(open('/task/workspace/invoice/__init__.py').read())
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])