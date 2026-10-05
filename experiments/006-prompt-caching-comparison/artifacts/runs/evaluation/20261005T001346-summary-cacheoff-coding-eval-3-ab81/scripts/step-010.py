p='/task/workspace/invoice/core.py'
s=open(p).read()
a=s.index('def tax_rate')
b=s.index('PREFIX =')
new='''def tax_rate(customer):
    if customer.get('tax_exempt') is True:
        return Decimal('0')
    return {'NZ': Decimal('0.15'), 'AU': Decimal('0.10'), 'US': Decimal('0')}.get(customer.get('region'), Decimal('0.12'))


def _bulk(q):
    if q >= 200:
        return Decimal('0.88')
    if q >= 50:
        return Decimal('0.95')
    return Decimal('1')


def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    sub = Decimal('0')
    for l in lines:
        q = l.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        p = Decimal(str(l['unit_price']))
        if p < 0:
            raise ValueError('negative price')
        sub += q * p * _bulk(q)
    disc = sub * discount_rate(lines, customer, sub)
    tax = (sub - disc) * tax_rate(customer)
    s, d, t = _r(sub), _r(disc), _r(tax)
    total = s - d + t
    return {'subtotal': str(s), 'discount': str(d), 'tax': str(t), 'total': str(_r(total))}


'''
s=s[:a]+new+s[b:]
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('Stage4 done.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])