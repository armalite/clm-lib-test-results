p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}","TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
s=s.replace("def tax_rate(customer):\n    return Decimal('0.10')","def tax_rate(customer):\n    if customer.get('tax_exempt') is True:\n        return Decimal('0')\n    return Decimal('0.10')")
s=s.replace("def compute_invoice(lines, customer):\n","""def validate(lines):
    if not lines:
        raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('qty')
        if Decimal(l['unit_price'])<0:
            raise ValueError('price')

def compute_invoice(lines, customer):
    validate(lines)
""")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage3 done: validation, tax_exempt, new tiers\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])