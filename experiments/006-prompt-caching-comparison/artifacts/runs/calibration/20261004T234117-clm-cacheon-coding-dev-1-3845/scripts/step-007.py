p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("from decimal import Decimal, ROUND_HALF_UP","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN")
s=s.replace("        sub+=_r(q*p)\n    disc=_r(sub*","        a=q*p\n        if q>=100: a*=Decimal('0.90')\n        sub+=a\n    disc=(sub*")
s=s.replace("    tax=_r((sub-disc)*rate)\n    tot=sub-disc+tax\n    return {'subtotal':str(_r(sub)),'discount':str(disc),'tax':str(tax),'total':str(_r(tot))}","    tax=(sub-disc)*rate\n    rs,rd,rt=_e(sub),_e(disc),_e(tax)\n    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(rs-rd+rt)}")
s=s.replace("def compute_invoice","def _e(x):\n    return x.quantize(Q, rounding=ROUND_HALF_EVEN)\n\ndef compute_invoice")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-1500:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stages1-3 implemented in invoice/core.py: validation ValueError; tier disc gold5 silver2; tax NZ15 AU10 US0 else12; stage3: bulk qty>=100 line*0.90, no line rounding, exact sub/disc/tax rounded half-even (_e), total=rs-rd+rt. format_money still NotImplemented. Check test result in last obs, then advance to stage 4.'}]}
json.dump(c,open('/task/workspace/context.json','w'))