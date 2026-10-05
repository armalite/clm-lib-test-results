p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("def tax_rate(customer):\n    return Decimal('0')","def tax_rate(customer):\n    return Decimal('0.10')")
s=s.replace("def format_money(amount, currency):\n    raise NotImplementedError","""PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}\n\ndef format_money(amount, currency):\n    if currency not in PFX:\n        raise ValueError('bad currency')\n    a=_r(Decimal(str(amount)))\n    sign='-' if a<0 else ''\n    return sign+PFX[currency]+str(abs(a))""")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])