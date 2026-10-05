import json,subprocess,sys,re
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("def tax_rate(lines, customer):\n    return Decimal('0')","def tax_rate(lines, customer):\n    return Decimal('0.10')")
s=s[:s.index('def format_money')]+'''PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError('currency')
    a=_r(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+PREFIX[currency]+str(abs(a))
'''
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
n='Stage1+2 done: invoice/core.py compute_invoice (round lines half-up, tier gold5%/silver2%, validation qty pos int, price>=0, nonempty; tax 10% on sub-disc). Hooks discount_rate(lines,customer,sub), tax_rate(lines,customer), validate. format_money(amount,currency) with PREFIX dict NZD/AUD/USD, -prefix for negatives, ValueError otherwise. Tests at /task/fixtures/current-tests.'
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':n}]},open('/task/workspace/context.json','w'))