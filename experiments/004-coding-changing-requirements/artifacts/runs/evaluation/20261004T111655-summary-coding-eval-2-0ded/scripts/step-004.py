p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("tax_rate = Decimal('0')","tax_rate = Decimal('0.10')")
s=s.replace('''def format_money(amount, currency):
    raise NotImplementedError''','''PFX = {'NZD': 'NZ$', 'AUD': 'A$', 'USD': 'US$'}


def format_money(amount, currency):
    if currency not in PFX:
        raise ValueError('bad currency')
    a = r2(Decimal(str(amount)))
    sign = '-' if a < 0 else ''
    return sign + PFX[currency] + str(abs(a))''')
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage2 done: tax 10%, format_money NZ$/A$/US$.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])