import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace('ROUND_HALF_UP','ROUND_HALF_EVEN')
s=s.replace('        sub+=r2(a)\n    disc=r2(sub*Decimal(0))\n    tax=r2((sub-disc)*Decimal(\'0.10\'))\n    tot=sub-disc+tax\n','        sub+=a\n    rate={\'gold\':Decimal(\'0.05\'),\'silver\':Decimal(\'0.02\')}.get((customer or {}).get(\'tier\'),Decimal(0))\n    d=sub*rate\n    t=(sub-d)*Decimal(\'0.10\')\n    sub,disc,tax=r2(sub),r2(d),r2(t)\n    tot=sub-disc+tax\n')
open(p,'w').write(s)
ctx={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stages1-3 done in invoice/core.py: compute_invoice (validation ValueError: empty lines, qty not positive int, negative unit_price; bulk qty>=200 x0.88 elif >=50 x0.95 per line, no line rounding; tier discount gold 5% silver 2% else 0 on exact subtotal; tax 10% of exact sub-disc; round sub/disc/tax half-even; total=sum of rounded; returns str dict subtotal/discount/tax/total). format_money unimplemented. Reqs in /task/fixtures/stage-N/REQUIREMENTS.md. Next: advance to stage 4 if tests pass.'}]}
json.dump(ctx,open('/task/workspace/context.json','w'))
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])