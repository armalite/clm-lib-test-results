p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("""        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('bad qty')""","""        if isinstance(q,bool) or not isinstance(q,int) or q<0:
            raise ValueError('bad qty')""")
s=s.replace("""        a=Decimal(q)*p""","""        if q==0:
            continue
        a=Decimal(q)*p""")
s=s.replace("""        sub+=r2(a)
    disc=r2(sub*TIER.get(customer.get('tier'),Decimal('0')))
    tax=r2((sub-disc)*TAX)
    tot=sub-disc+tax
    return {'subtotal':str(r2(sub)),'discount':str(disc),'tax':str(tax),'total':str(r2(tot))}""","""        sub+=a
    disc=sub*TIER.get(customer.get('tier'),Decimal('0'))
    tax=Decimal('0') if customer.get('tax_exempt') is True else (sub-disc)*TAX
    rs,rd,rt=b2(sub),b2(disc),b2(tax)
    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(rs-rd+rt)}""")
s=s.replace("from decimal import Decimal, ROUND_HALF_UP","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN")
s=s.replace("TIER=","def b2(x):\n    return x.quantize(Q, rounding=ROUND_HALF_EVEN)\n\nTIER=",1)
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2500:])
n='All 4 stages released. Stage4 implemented in invoice/core.py: tax_exempt, banker rounding on exact sub/disc/tax, qty0 skipped. Next: final if tests OK.'
json.dump({'format':'clm-context/v1','entries':[{'id':'sum1','role':'summary','body':n}]},open('/task/workspace/context.json','w'))