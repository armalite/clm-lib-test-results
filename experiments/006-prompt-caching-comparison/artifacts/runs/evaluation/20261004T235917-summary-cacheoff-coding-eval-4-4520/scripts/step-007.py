p='/task/workspace/invoice/core.py';s=open(p).read()
s=s.replace("    if int(line['qty']) >= 100:\n        amt = amt * Decimal('0.90')","    q = int(line['qty'])\n    if q >= 200:\n        amt = amt * Decimal('0.88')\n    elif q >= 50:\n        amt = amt * Decimal('0.95')")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError","""PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError('bad currency')
    a = r2(Decimal(str(amount)))
    sign = '-' if a < 0 else ''
    return sign + PREFIX[currency] + str(abs(a))""")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('Stage3 done: format_money, bulk 200->0.88, 50->0.95.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])