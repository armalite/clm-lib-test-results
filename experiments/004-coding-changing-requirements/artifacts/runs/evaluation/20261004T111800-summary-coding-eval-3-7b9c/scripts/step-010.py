src=open('/task/workspace/invoice/core.py').read()
src=src.replace("(Decimal('0.90') if l['qty'] >= 100 else 1)","_bulk(l['qty'])")
src=src.replace("def compute_invoice(lines, customer):\n","""def _bulk(q):
    if q >= 200:
        return Decimal('0.88')
    if q >= 50:
        return Decimal('0.95')
    return Decimal('1')


def _validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        if Decimal(str(l.get('unit_price'))) < 0:
            raise ValueError('negative price')


def compute_invoice(lines, customer):
    _validate(lines)
""")
import re
src=re.sub(r"def tax_rate\(customer\):\n    return [^\n]*","REGION = {'NZ': Decimal('0.15'), 'AU': Decimal('0.10'), 'US': Decimal('0')}\n\n\ndef tax_rate(customer):\n    return REGION.get(customer.get('region'), Decimal('0.12'))",src)
open('/task/workspace/invoice/core.py','w').write(src)
open('/task/workspace/NOTES.md','a').write('stage4 done.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:]);print('REGION' in src)