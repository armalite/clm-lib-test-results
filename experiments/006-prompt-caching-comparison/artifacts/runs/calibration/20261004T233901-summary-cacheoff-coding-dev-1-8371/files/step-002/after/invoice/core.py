"""Invoice core."""
from decimal import Decimal, ROUND_HALF_UP, InvalidOperation

Q = Decimal('0.01')

def r2(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)

def discount_rate(lines, customer, subtotal):
    return Decimal('0')

def tax_rate(customer):
    return Decimal('0.10')

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
        sub += r2(q * p)
    disc = r2(sub * discount_rate(lines, customer, sub))
    tax = r2((sub - disc) * tax_rate(customer))
    total = sub - disc + tax
    return {k: str(r2(v)) for k, v in (('subtotal', sub), ('discount', disc), ('tax', tax), ('total', total))}

def format_money(amount, currency):
    raise NotImplementedError
