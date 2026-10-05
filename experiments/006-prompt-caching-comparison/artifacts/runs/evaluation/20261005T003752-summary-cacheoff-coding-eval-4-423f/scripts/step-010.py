p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("from decimal import Decimal, ROUND_HALF_UP","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN")
s=s.replace("        amt*=Decimal('0.95')\n    return r2(amt)","        amt*=Decimal('0.95')\n    return amt")
s=s.replace("or q<=0:","or q<0:")
s=s.replace("""    subtotal=sum((line_amount(l) for l in lines), Decimal('0.00'))
    discount=r2(subtotal*discount_rate(customer, subtotal))
    tax=r2((subtotal-discount)*tax_rate(customer))
    total=subtotal-discount+tax
    return {k:str(r2(v))""","""    sub=sum((line_amount(l) for l in lines if l['qty']!=0), Decimal('0'))
    disc=sub*discount_rate(customer, sub)
    tx=Decimal('0') if customer.get('tax_exempt') is True else (sub-disc)*tax_rate(customer)
    he=lambda x:x.quantize(Q, rounding=ROUND_HALF_EVEN)
    subtotal,discount,tax=he(sub),he(disc),he(tx)
    total=subtotal-discount+tax
    return {k:str(he(v))""")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage4 done.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
print('he(' in s, 'q<0:' in s, 'return amt' in s)