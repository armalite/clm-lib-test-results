p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("""    if int(line['qty']) >= 100:
        amt = amt * Decimal('0.90')""","""    q = int(line['qty'])
    if q >= 200:
        amt = amt * Decimal('0.88')
    elif q >= 50:
        amt = amt * Decimal('0.95')""")
s=s.replace("""def format_money(amount, currency):
    raise NotImplementedError""","""_PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}


def format_money(amount, currency):
    if currency not in _PREFIX:
        raise ValueError('unknown currency')
    d = r2(Decimal(str(amount)))
    sign = '-' if d < 0 else ''
    return sign + _PREFIX[currency] + str(abs(d))""")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage3 done: format_money, bulk 200->0.88, 50->0.95.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])