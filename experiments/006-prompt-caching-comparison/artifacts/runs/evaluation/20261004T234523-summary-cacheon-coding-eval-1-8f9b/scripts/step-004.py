p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("""    if int(line['qty']) >= 100:
        amt = amt * Decimal('0.90')""","""    q = int(line['qty'])
    if q >= 200:
        amt = amt * Decimal('0.88')
    elif q >= 50:
        amt = amt * Decimal('0.95')""")
s=s.replace("""def compute_invoice(lines, customer):
""","""def validate(lines):
    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        try:
            p = Decimal(str(l['unit_price']))
        except Exception:
            raise ValueError('bad price')
        if p < 0:
            raise ValueError('negative price')

def compute_invoice(lines, customer):
    validate(lines)
""")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('Stage2 done: validation, bulk 200->0.88, 50->0.95.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])