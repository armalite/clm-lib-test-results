p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace('{"gold":Decimal("0.05"),"silver":Decimal("0.02")}','{"gold":Decimal("0.08"),"platinum":Decimal("0.10"),"silver":Decimal("0.02")}')
open(p,'w').write(s)
import subprocess,sys
q=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(q.stderr[-1500:])
open('/task/workspace/NOTES.md','a').write('stage5 done: gold 8 platinum 10 silver 2\n')