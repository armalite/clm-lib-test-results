"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN, InvalidOperation

Q = Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def discount_rate(lines, customer, subtotal):
    return {'platinum': Decimal('0.10'), 'gold': Decimal('0.07'), 'silver': Decimal('0.03')}.get(customer.get('tier'), Decimal('0'))

def tax_rate(customer):
    return {'NZ': Decimal('0.15'), 'AU': Decimal('0.10'), 'US': Decimal('0')}.get(customer.get('region'), Decimal('0.12'))

def compute_invoice(lines, customer):
    if not lines:
        raise ValueError('empty lines')
    sub = Decimal('0')
    for ln in lines:
        q = ln.get('qty')
        if isinstance(q, bool) or not isinstance(q, int) or q <= 0:
            raise ValueError('bad qty')
        try:
            p = Decimal(str(ln.get('unit_price')))
        except InvalidOperation:
            raise ValueError('bad price')
        if not p.is_finite() or p < 0:
            raise ValueError('bad price')
        amt = q * p
        if q >= 100:
            amt = amt * Decimal('0.90')
        sub += amt
    edisc = sub * discount_rate(lines, customer, sub)
    etax = (sub - edisc) * tax_rate(customer)
    sub = sub.quantize(Q, rounding=ROUND_HALF_EVEN)
    disc = edisc.quantize(Q, rounding=ROUND_HALF_EVEN)
    tax = etax.quantize(Q, rounding=ROUND_HALF_EVEN)
    total = sub - disc + tax
    return {k: str(r2(v)) for k, v in (('subtotal', sub), ('discount', disc), ('tax', tax), ('total', total))}

def format_money(amount, currency):
    prefixes = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}
    if currency not in prefixes:
        raise ValueError('unsupported currency')
    try:
        d = Decimal(str(amount))
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError('bad amount')
    if not d.is_finite():
        raise ValueError('bad amount')
    d = d.quantize(Decimal('0.01'), rounding=ROUND_HALF_EVEN)
    neg = d < 0
    return ('-' if neg else '') + prefixes[currency] + str(abs(d))
