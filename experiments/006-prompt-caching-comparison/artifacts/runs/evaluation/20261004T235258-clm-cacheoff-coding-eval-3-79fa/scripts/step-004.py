import json,subprocess,sys
import re
p='/task/workspace/invoice/core.py'
c=open(p).read()
c=c.replace('''def tax_rate(customer):\n    return Decimal('0.10')''','''def tax_rate(customer):\n    if customer.get('tax_exempt') is True: return Decimal('0')\n    return Decimal('0.10')''')
c=c.replace('''def discount_rate(customer, subtotal):\n    return Decimal('0')''','''def discount_rate(customer, subtotal):\n    return {'gold':Decimal('0.05'),'silver':Decimal('0.02')}.get(customer.get('tier'),Decimal('0'))''')
start=c.index('def compute_invoice'); end=c.index('PREFIX=')
c=c[:start]+'''def _he(x):
    return Decimal(x).quantize(Q, rounding=ROUND_HALF_EVEN)

def compute_invoice(lines, customer):
    sub=sum((Decimal(str(l['qty']))*Decimal(str(l['unit_price'])) for l in lines), Decimal('0'))
    disc=sub*discount_rate(customer, sub)
    tax=(sub-disc)*tax_rate(customer)
    rs,rd,rt=_he(sub),_he(disc),_he(tax)
    tot=rs-rd+rt
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(tot)}

'''+c[end:]
c=c.replace('ROUND_HALF_UP\n','ROUND_HALF_UP, ROUND_HALF_EVEN\n',1)
open(p,'w').write(c)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'invoice/core.py. Stage1: format_money PREFIX dict (NZ$,A$,US$), negative -> -prefix, unknown ValueError (half-up _r). Stage2: tier discount gold5%/silver2%; tax_exempt True -> tax 0; no line rounding, exact sub/disc/tax then half-even (_he) each, total=sum of rounded. tax 10%. Tests: unittest discover -s /task/fixtures/current-tests.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))