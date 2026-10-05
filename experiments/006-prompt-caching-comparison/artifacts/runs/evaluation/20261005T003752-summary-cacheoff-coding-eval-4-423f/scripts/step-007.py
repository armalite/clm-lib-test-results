p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    if line['qty']>=100:\n        amt*=Decimal('0.90')\n","    if line['qty']>=200:\n        amt*=Decimal('0.88')\n    elif line['qty']>=50:\n        amt*=Decimal('0.95')\n")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError\n","""PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PREFIX:
        raise ValueError('bad currency')
    a=r2(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+PREFIX[currency]+str(abs(a))
""")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage3 done: format_money NZ$/A$/US$, bulk >=200 x0.88, >=50 x0.95.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])