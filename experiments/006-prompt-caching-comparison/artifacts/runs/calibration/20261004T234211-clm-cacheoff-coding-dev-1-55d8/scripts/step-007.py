p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("from decimal import Decimal, ROUND_HALF_UP","from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN")
s=s.replace("        sub+=_r(q*p)","        a=q*p\n        if q>=100:\n            a=a*Decimal('0.90')\n        sub+=a")
s=s.replace("    disc=_r(sub*","    disc=(sub*")
s=s.replace("    tax=_r((sub-disc)*","    tax=((sub-disc)*")
s=s.replace("    tot=sub-disc+tax\n    return {'subtotal':str(_r(sub)),'discount':str(disc),'tax':str(tax),'total':str(_r(tot))}","    rs,rd,rt=_e(sub),_e(disc),_e(tax)\n    return {'subtotal':str(rs),'discount':str(rd),'tax':str(rt),'total':str(rs-rd+rt)}")
s=s.replace("def compute_invoice","def _e(x):\n    return x.quantize(Q, rounding=ROUND_HALF_EVEN)\n\ndef compute_invoice")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
c={'format':'clm-context/v1','entries':[{'id':'sum1','role':'summary','body':'Stages1-3 in invoice/core.py: validation (empty, qty pos int non-bool, price>=0); bulk qty>=100 line*0.90; no line rounding; exact sub, disc (gold .05 silver .02), tax (NZ .15 AU .10 US 0 else .12) on sub-disc; each rounded half-even via _e; total=rs-rd+rt. format_money still NotImplemented. Check test result then advance to stage 4.'}]}
json.dump(c,open('/task/workspace/context.json','w'))