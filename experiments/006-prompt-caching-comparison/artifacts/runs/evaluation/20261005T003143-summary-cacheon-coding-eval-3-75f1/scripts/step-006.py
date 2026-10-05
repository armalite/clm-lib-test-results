src=open('/task/workspace/invoice/core.py').read()
src=src.replace('from decimal import Decimal, ROUND_HALF_UP','from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN')
start=src.index('def _discount_rate');end=src.index('PREFIX =')
new='''def _e(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)


def _discount_rate(lines, customer, subtotal):
    return {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}.get(customer.get('tier'), Decimal('0'))


def _tax_rate(customer):
    if customer.get('tax_exempt') is True:
        return Decimal('0')
    return Decimal('0.10')


def compute_invoice(lines, customer):
    sub = sum((int(l['qty']) * Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))
    disc = sub * _discount_rate(lines, customer, sub)
    tax = (sub - disc) * _tax_rate(customer)
    s, d, t = _e(sub), _e(disc), _e(tax)
    total = s - d + t
    return {'subtotal': str(s), 'discount': str(d), 'tax': str(t), 'total': str(_e(total))}


'''
src=src[:start]+new+src[end:]
open('/task/workspace/invoice/core.py','w').write(src)
open('/task/workspace/NOTES.md','a').write('Stage2 done: tier gold5/silver2, tax_exempt True->0, rounding exact then half-even each of sub/disc/tax.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])