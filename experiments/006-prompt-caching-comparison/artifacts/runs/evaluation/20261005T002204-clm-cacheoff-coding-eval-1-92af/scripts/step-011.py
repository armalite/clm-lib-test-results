import re,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
ls=s.splitlines()
print('\n'.join(ls[15:19]));print('\n'.join(ls[54:]))
i=s.index('def tax_rate(customer):');j=s.index('def line_amount')
s=s[:i]+"""def tax_rate(customer):
    c = customer or {}
    if c.get('tax_exempt') is True:
        return Decimal('0')
    return {'NZ': Decimal('0.15'), 'AU': Decimal('0.10'), 'US': Decimal('0')}.get(c.get('region'), Decimal('0.12'))


"""+s[j:]
k=s.index('def format_money')
s=s[:k]+"""def format_money(amount, currency):
    pre = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}
    if currency not in pre:
        raise ValueError('unsupported currency: %r' % (currency,))
    a = r2(Decimal(str(amount)))
    sign = '-' if a < 0 else ''
    return '%s%s%s' % (sign, pre[currency], format(abs(a), '.2f'))
"""
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])