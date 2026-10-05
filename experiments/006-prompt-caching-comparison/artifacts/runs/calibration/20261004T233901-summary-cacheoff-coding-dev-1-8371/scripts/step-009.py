p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("{'gold': Decimal('0.05'), 'silver': Decimal('0.02')}","{'platinum': Decimal('0.10'), 'gold': Decimal('0.07'), 'silver': Decimal('0.03')}")
s=s.replace("""def format_money(amount, currency):
    raise NotImplementedError""","""def format_money(amount, currency):
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
    return ('-' if neg else '') + prefixes[currency] + str(abs(d))""")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage4 done\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])