p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("""def _tax_rate(customer):
    return Decimal('0.10')""","""REG={'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}

def _tax_rate(customer):
    c=customer if isinstance(customer,dict) else {}
    if c.get('tax_exempt') is True:
        return Decimal('0')
    return REG.get(c.get('region'),Decimal('0.12'))""")
s=s.replace("""def format_money(amount, currency):
    raise NotImplementedError""","""PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PFX:
        raise ValueError('bad currency')
    a=Decimal(str(amount)).quantize(Q, rounding=ROUND_HALF_EVEN)
    neg=a<0
    return ('-' if neg else '')+PFX[currency]+str(abs(a))""")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
print(open('/task/workspace/invoice/__init__.py').read())
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'All 4 stages released. Stage4 implemented in core.py: region tax NZ15 AU10 US0 else12, tax_exempt->0, format_money. Check tests then final.'}]}
json.dump(c,open('/task/workspace/context.json','w'))