p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("""def tax_rate(customer):
    return Decimal('0.10')""","""def tax_rate(customer):
    if customer.get('tax_exempt') is True:
        return Decimal('0')
    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(customer.get('region'),Decimal('0.12'))""")
s=s.replace("""def format_money(amount, currency):
    raise NotImplementedError""","""def format_money(amount, currency):
    pre={'NZD':'NZ$','AUD':'A$','USD':'US$'}
    if currency not in pre:
        raise ValueError('bad currency')
    a=r2(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+pre[currency]+str(abs(a))""")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('Stage4 done: region tax, exempt, format_money.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])