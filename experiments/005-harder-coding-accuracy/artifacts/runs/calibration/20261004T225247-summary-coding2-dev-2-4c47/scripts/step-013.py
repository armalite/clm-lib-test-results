p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("q<=0: raise","q<0: raise")
s=s.replace("def compute_invoice(lines, customer):\n    _validate(lines)\n","BULK=50\ndef compute_invoice(lines, customer):\n    _validate(lines)\n    lines=[l for l in lines if l['qty']!=0]\n    if not lines: raise ValueError('all lines ignored')\n")
s=s.replace(">=100 else",">=BULK else").replace("<100),","<BULK),")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage5 done: BULK=50, qty0 ignored\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])