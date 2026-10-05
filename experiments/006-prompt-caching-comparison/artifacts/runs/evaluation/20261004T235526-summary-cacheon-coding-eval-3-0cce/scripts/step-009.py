p='/task/workspace/invoice/core.py'
c=open(p).read()
c=c.replace("(Decimal('0.90') if l['qty'] >= 100 else 1)","bulk(l['qty'])")
c=c.replace("    return Decimal('0.10')","    return {'NZ': Decimal('0.15'), 'AU': Decimal('0.10'), 'US': Decimal('0')}.get(customer.get('region'), Decimal('0.12'))")
c=c.replace("def compute_invoice(lines, customer):\n","""def bulk(q):
    if q >= 200:
        return Decimal('0.88')
    if q >= 50:
        return Decimal('0.95')
    return Decimal('1')

def validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        try:
            p = Decimal(str(l.get('unit_price')))
        except Exception:
            raise ValueError('bad price')
        if not p.is_finite() or p < 0:
            raise ValueError('negative price')

def compute_invoice(lines, customer):
    validate(lines)
""")
open(p,'w').write(c)
open('/task/workspace/NOTES.md','a').write('stage4 done: validation, region tax, bulk 200->0.88 50->0.95.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])