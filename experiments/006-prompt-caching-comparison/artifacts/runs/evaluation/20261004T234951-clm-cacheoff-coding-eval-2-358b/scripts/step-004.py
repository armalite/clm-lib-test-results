import subprocess,sys,json,re
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("def tax_rate(customer):\n    return Decimal('0')","def tax_rate(customer):\n    return Decimal('0.10')")
s=s[:s.index('def format_money')]+'''PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError('bad currency')
    a=r2(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+PREFIX[currency]+str(abs(a))
'''
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stages1-2 done in invoice/core.py: r2 half-up per line, tier discount gold5%/silver2% via discount_rate(customer,subtotal), tax_rate(customer)=10% on (sub-disc), ValueError validation (empty, qty non-positive int/bool, negative price). format_money(amount,currency) via PREFIX dict NZD NZ$/AUD A$/USD US$, 2dp, -before prefix, else ValueError. Next: advance.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))