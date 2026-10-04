code='''from decimal import Decimal, ROUND_HALF_UP

Q = Decimal("0.01")


def _r(x):
    return x.quantize(Q, rounding=ROUND_HALF_UP)


def discount_rate(lines, customer, subtotal):
    return Decimal(0)


def tax_rate(customer):
    return Decimal("0.10")


def compute_invoice(lines, customer):
    subtotal = sum((_r(int(l["qty"]) * Decimal(str(l["unit_price"]))) for l in lines), Decimal(0))
    subtotal = _r(subtotal)
    discount = _r(subtotal * discount_rate(lines, customer, subtotal))
    tax = _r((subtotal - discount) * tax_rate(customer))
    total = subtotal - discount + tax
    return {"subtotal": str(subtotal), "discount": str(discount), "tax": str(tax), "total": str(_r(total))}


PREFIX = {"NZD": "NZ$", "AUD": "A$", "USD": "US$"}


def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError(currency)
    a = _r(Decimal(str(amount)))
    sign = "-" if a < 0 else ""
    return f"{sign}{PREFIX[currency]}{abs(a)}"
'''
open('/task/workspace/invoice/core.py','w').write(code)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 done: invoice/core.py has _r (half-up 2dp), discount_rate(lines,customer,subtotal)=0, tax_rate(customer)=0.10, compute_invoice, format_money(PREFIX NZD NZ$/AUD A$/USD US$, -before prefix, else ValueError). Rounding: line amounts rounded, discount & tax rounded.'}]},open('/task/workspace/context.json','w'))