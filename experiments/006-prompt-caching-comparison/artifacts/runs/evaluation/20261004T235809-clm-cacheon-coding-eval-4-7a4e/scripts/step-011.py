p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("    return r2(a)\n\ndef discount","    return a\n\ndef discount")
s=s.replace("isinstance(q,int) or q<=0","isinstance(q,int) or q<0")
old=s[s.index('def compute_invoice'):s.index('PFX=')]
new='''def compute_invoice(lines, customer):
    validate(lines)
    ls=[l for l in lines if l['qty']!=0]
    sub=sum((line_amount(l,customer) for l in ls),Decimal(0))
    disc=sub*discount_rate(customer,sub,ls)
    tax=(sub-disc)*tax_rate(customer,ls)
    if customer.get('tax_exempt') is True:
        tax=Decimal(0)
    sub,disc,tax=[x.quantize(Q,rounding=ROUND_HALF_EVEN) for x in (sub,disc,tax)]
    tot=sub-disc+tax
    return {k:str(v.quantize(Q)) for k,v in [('subtotal',sub),('discount',disc),('tax',tax),('total',tot)]}

'''
s=s.replace(old,new).replace('ROUND_HALF_UP\n','ROUND_HALF_UP, ROUND_HALF_EVEN\n',1)
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
json.dump({'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'All 4 stages implemented in invoice/core.py (stage4: no line rounding, half-even on sub/disc/tax, tax_exempt, qty0 skipped). Check test result then final.'}]},open('/task/workspace/context.json','w'))