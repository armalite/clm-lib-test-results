p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace('def _tax_rate(customer):\n    return Decimal(0)','def _tax_rate(customer):\n    return Decimal("0.10")')
s=s.replace('def format_money(amount, currency):\n    raise NotImplementedError','''_PFX = {"NZD": "NZ$", "AUD": "A$", "USD": "US$"}


def format_money(amount, currency):
    if currency not in _PFX:
        raise ValueError("unknown currency")
    a = _r(Decimal(str(amount)))
    sign = "-" if a < 0 else ""
    return sign + _PFX[currency] + str(abs(a))''')
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('Stage2 done: tax 10% (_tax_rate), format_money prefixes.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])