import subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace('ROUND_HALF_UP)\n\nQ','ROUND_HALF_EVEN\n\nQ',1) if False else s
s=s.replace('from decimal import Decimal, ROUND_HALF_UP','from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN')
s=s.replace('def r2(x): return x.quantize(Q, rounding=ROUND_HALF_UP)','def r2(x): return x.quantize(Q, rounding=ROUND_HALF_EVEN)')
s=s.replace('sub+=r2(a)','sub+=a').replace('elig+=r2(a)','elig+=a').replace('disc=r2(elig*rate)','disc=elig*rate')
s=s.replace('tax=r2((sub-disc)*trate)\n    tot=sub-disc+ship+tax','tax=(sub-disc+ship)*trate\n    sub,disc,tax=r2(sub),r2(disc),r2(tax)\n    tot=sub-disc+ship+tax')
open(p,'w').write(s)
print(s[-700:])
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])