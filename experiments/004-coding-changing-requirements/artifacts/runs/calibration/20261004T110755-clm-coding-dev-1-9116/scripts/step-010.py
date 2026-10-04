p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("{'gold':Decimal('0.05'),'silver':Decimal('0.02')}","{'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
i=s.index('def format_money')
s=s[:i]+'''def format_money(amount, currency):
    p={'NZD':'NZ$','AUD':'A$','USD':'US$'}
    if currency not in p:
        raise ValueError(currency)
    d=Decimal(str(amount)).quantize(Decimal('0.01'),rounding=ROUND_HALF_EVEN)
    neg=d<0
    return ('-' if neg else '')+p[currency]+str(abs(d))
'''
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
print(open(p).read()[-400:])