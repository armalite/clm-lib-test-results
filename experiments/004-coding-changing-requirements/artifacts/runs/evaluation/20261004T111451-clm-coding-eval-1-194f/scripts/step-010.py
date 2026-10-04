import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
ls=s.splitlines()
print('\n'.join(ls[14:17]));print('\n'.join(ls[40:]))
i=s.index('def tax_rate(customer):');j=s.index('def line_amount')
s=s[:i]+"""def tax_rate(customer):
    c=customer or {}
    if c.get('tax_exempt') is True: return Decimal('0')
    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(c.get('region'),Decimal('0.12'))

"""+s[j:]
i=s.index('def format_money')
s=s[:i]+"""def format_money(amount, currency):
    pre={'NZD':'NZ$','AUD':'A$','USD':'US$'}
    if currency not in pre: raise ValueError('currency')
    d=r2(Decimal(str(amount)))
    sign='-' if d<0 else ''
    return sign+pre[currency]+str(abs(d))
"""
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
c={'format':'clm-context/v1','entries':[{'id':'sum1','role':'summary','body':'All 4 stages released. core.py: stages1-3 done; stage4 implemented in step 10 (tax_rate region NZ15/AU10/US0/else12, tax_exempt True->0, format_money NZ$/A$/US$ with -prefix, ValueError other). Check last obs test result; if OK, final.'}]}
json.dump(c,open('/task/workspace/context.json','w'))