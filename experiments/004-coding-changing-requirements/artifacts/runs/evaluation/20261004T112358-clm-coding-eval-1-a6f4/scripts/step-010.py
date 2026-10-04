import re,subprocess,sys
p='/task/workspace/invoice/core.py';c=open(p).read()
L=c.splitlines()
print('\n'.join(L[9:12]));print('\n'.join(L[38:]))
i=c.index('def tax_rate(customer):');j=c.index('def line_amount')
c=c[:i]+"""def tax_rate(customer):
    cu=customer or {}
    if cu.get('tax_exempt') is True: return Decimal('0')
    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(cu.get('region'),Decimal('0.12'))

"""+c[j:]
k=c.index('def format_money')
c=c[:k]+"""def format_money(amount, currency):
    pre={'NZD':'NZ$','AUD':'A$','USD':'US$'}
    if currency not in pre: raise ValueError('bad currency')
    a=Decimal(str(amount)).quantize(Q,rounding=ROUND_HALF_EVEN)
    s='-' if a<0 else ''
    return s+pre[currency]+str(abs(a))
"""
open(p,'w').write(c)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])