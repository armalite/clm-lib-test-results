p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("q<=0:","q<0:")
s=s.replace("        a=Decimal(q)*p","        if q==0:\n            continue\n        a=Decimal(q)*p")
s=s.replace("        sub+=r2(a)\n    sub=r2(sub)\n    disc=r2(sub*TIER.get(customer.get('tier'),Decimal('0')))\n    tax=r2((sub-disc)*TAX)\n    total=sub-disc+tax\n","        sub+=a\n    from decimal import ROUND_HALF_EVEN\n    be=lambda x:x.quantize(Q,rounding=ROUND_HALF_EVEN)\n    d=sub*TIER.get(customer.get('tier'),Decimal('0'))\n    t=Decimal('0') if customer.get('tax_exempt') is True else (sub-d)*TAX\n    sub,disc,tax=be(sub),be(d),be(t)\n    total=sub-disc+tax\n")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])