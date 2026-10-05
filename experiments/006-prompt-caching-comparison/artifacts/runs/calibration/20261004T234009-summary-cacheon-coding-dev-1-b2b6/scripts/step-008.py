import re
p='/task/workspace/invoice/core.py'
s=open(p).read()
i=s.index('def format_money')
j=s.find('\ndef ',i+5)
new='''def format_money(amount, currency):
    pre={'NZD':'NZ$','AUD':'A$','USD':'US$'}
    if currency not in pre: raise ValueError('unsupported currency')
    d=Decimal(str(amount)).quantize(Q,rounding=ROUND_HALF_EVEN)
    sign='-' if d<0 else ''
    return sign+pre[currency]+str(abs(d))
'''
s=s[:i]+new+(s[j:] if j!=-1 else '')
open(p,'w').write(s)
for l in s.splitlines():
    if 'gold' in l or 'silver' in l: print(l)
