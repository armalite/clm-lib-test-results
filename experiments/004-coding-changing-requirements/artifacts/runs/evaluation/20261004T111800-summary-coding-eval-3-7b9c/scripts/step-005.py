src=open('/task/workspace/invoice/core.py').read()
src=src.replace("from decimal import Decimal, ROUND_HALF_UP","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN")
src=src.replace("""def discount_rate(lines, customer, subtotal):
    return Decimal('0')""","""def _re(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)


TIER = {'gold': Decimal('0.05'), 'silver': Decimal('0.02')}


def discount_rate(lines, customer, subtotal):
    return TIER.get(customer.get('tier'), Decimal('0'))""")
old=src[src.index('def compute_invoice'):src.index('PREFIX =')]
new='''def compute_invoice(lines, customer):
    sub = sum((Decimal(l['qty']) * Decimal(l['unit_price']) for l in lines), Decimal('0'))
    disc = sub * discount_rate(lines, customer, sub)
    tax = (sub - disc) * tax_rate(customer)
    if customer.get('tax_exempt') is True:
        tax = Decimal('0')
    s, d, t = _re(sub), _re(disc), _re(tax)
    total = s - d + t
    return {'subtotal': str(s), 'discount': str(d), 'tax': str(t), 'total': str(_re(total))}


'''
src=src.replace(old,new)
open('/task/workspace/invoice/core.py','w').write(src)
open('/task/workspace/NOTES.md','a').write('stage2 done: tier discount gold5/silver2, tax_exempt, half-even exact rounding.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])