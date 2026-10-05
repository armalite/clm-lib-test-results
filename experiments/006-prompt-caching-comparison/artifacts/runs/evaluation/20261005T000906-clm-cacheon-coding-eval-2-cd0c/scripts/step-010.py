import subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("        if q==0:\n            continue\n        p=Decimal(str(l['unit_price']))\n        if p<0:\n            raise ValueError('price')\n","        p=Decimal(str(l['unit_price']))\n        if p<0:\n            raise ValueError('price')\n        if q==0:\n            continue\n")
s=s.replace("    tax=_r((sub-disc)*rate)","    if customer.get('tax_exempt') is True:\n        rate=Decimal('0')\n    tax=_r((sub-disc)*rate)")
s=s.replace("PFX[currency]+str(abs(a))","PFX[currency]+'{:,.2f}'.format(abs(a))")
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])