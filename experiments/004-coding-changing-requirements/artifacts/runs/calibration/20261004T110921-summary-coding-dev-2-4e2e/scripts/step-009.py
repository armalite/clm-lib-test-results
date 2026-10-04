p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    return Decimal('0.10')\n\ndef validate","    return {'NZ':Decimal('0.15'),'AU':Decimal('0.10'),'US':Decimal('0')}.get(customer.get('region'),Decimal('0.12'))\n\ndef line_amount(l):\n    a=Decimal(l['qty'])*Decimal(l['unit_price'])\n    if l['qty']>=100:\n        a=a*Decimal('0.90')\n    return r2(a)\n\ndef validate")
s=s.replace("r2(Decimal(l['qty'])*Decimal(l['unit_price']))","line_amount(l)")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage4 done\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])