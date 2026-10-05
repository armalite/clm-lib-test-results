import subprocess,sys,json
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("from decimal import Decimal, ROUND_HALF_UP","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN")
s=s.replace("""def discount_rate(lines, customer, subtotal):
    return Decimal('0')""","""def discount_rate(lines, customer, subtotal):
    return {'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get((customer or {}).get('tier'),Decimal('0'))

def _b(x):
    return x.quantize(Q, rounding=ROUND_HALF_EVEN)""")
old=s[s.index('def compute_invoice'):s.index('_P=')]
new='''def compute_invoice(lines, customer):
    customer=customer or {}
    sub=sum((int(l['qty'])*Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))
    disc=sub*discount_rate(lines, customer, sub)
    tax=(sub-disc)*tax_rate(customer)
    if customer.get('tax_exempt') is True:
        tax=Decimal('0')
    rs,rd,rt=_b(sub),_b(disc),_b(tax)
    total=rs-rd+rt
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(total)}

'''
s=s.replace(old,new)
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1+2 done in invoice/core.py: discount_rate tier gold 5%/silver 2%; tax_exempt True->tax 0; exact sums then half-even round (_b) of subtotal/discount/tax, total=sum of rounded; tax_rate(customer)=0.10; format_money (NZ$/A$/US$, -prefix, half-up _r, ValueError). Reqs at /task/fixtures/stage-N/REQUIREMENTS.md. Next: advance to stage 3.'}]}
json.dump(c,open('/task/workspace/context.json','w'))