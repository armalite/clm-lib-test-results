p='/task/workspace/invoice/core.py';s=open(p).read()
s=s.replace("from decimal import Decimal, ROUND_HALF_UP","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN")
s=s.replace("a=Decimal(l['qty'])*Decimal(l['unit_price'])","a=Decimal(l['qty'])*Decimal(str(l['unit_price']))")
s=s.replace("    return r2(a)\n","    return a\n")
s=s.replace("q<=0: raise","q<0: raise")
s=s.replace("sub=sum((line_amount(l) for l in lines),Decimal(0))\n    disc=r2(sub*discount_rate(customer,sub))\n    tax=r2((sub-disc)*tax_rate(customer))\n    tot=sub-disc+tax","lines=[l for l in lines if l['qty']!=0]\n    sub=sum((line_amount(l) for l in lines),Decimal(0))\n    disc=sub*discount_rate(customer,sub)\n    tax=Decimal(0) if customer.get('tax_exempt') is True else (sub-disc)*tax_rate(customer)\n    be=lambda x:x.quantize(C,rounding=ROUND_HALF_EVEN)\n    sub,disc,tax=be(sub),be(disc),be(tax)\n    tot=sub-disc+tax")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])