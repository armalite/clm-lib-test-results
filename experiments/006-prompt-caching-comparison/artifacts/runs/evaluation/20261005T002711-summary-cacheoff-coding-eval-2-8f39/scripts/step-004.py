p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("def tax_rate(lines, customer):\n    return Decimal('0')","def tax_rate(lines, customer):\n    return Decimal('0.10')")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError",'''PREFIX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError('bad currency')
    a = _r(Decimal(str(amount)))
    sign = '-' if a < 0 else ''
    return sign + PREFIX[currency] + str(abs(a))''')
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage2 done: tax 10%, format_money\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])