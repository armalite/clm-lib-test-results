p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}","TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
s=s.replace("def tax_rate(customer):\n    return Decimal('0')","def tax_rate(customer):\n    return Decimal('0.10')")
s=s.replace("def compute_invoice(lines, customer):\n","""def validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('bad qty')
        try:
            pr=Decimal(str(l['unit_price']))
        except Exception:
            raise ValueError('bad price')
        if not pr.is_finite() or pr<0:
            raise ValueError('negative price')

def compute_invoice(lines, customer):
    validate(lines)
""")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage2 done: tax 10%, validation, tiers plat10 gold7 silver3.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])