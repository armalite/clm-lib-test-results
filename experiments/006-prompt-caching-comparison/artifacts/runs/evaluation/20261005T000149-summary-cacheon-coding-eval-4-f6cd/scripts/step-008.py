p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("        if q>=100: a*=Decimal('0.90')\n","        if q>=200: a*=Decimal('0.88')\n        elif q>=50: a*=Decimal('0.95')\n")
i=s.index('def format_money')
s=s[:i]+'''PREFIX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PREFIX: raise ValueError('unsupported currency')
    d=r2(Decimal(str(amount)))
    sign='-' if d<0 else ''
    return sign+PREFIX[currency]+str(abs(d))
'''
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('\nStage3: bulk 200->0.88, 50->0.95; format_money(amount,currency) NZ$/A$/US$, neg -prefix, else ValueError.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])