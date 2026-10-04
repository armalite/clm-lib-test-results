src=open('/task/workspace/invoice/core.py').read()
src=src.replace("return sign + PREFIX[currency] + str(abs(a))","return sign + PREFIX[currency] + '{:,.2f}'.format(abs(a))")
open('/task/workspace/invoice/core.py','w').write(src)
open('/task/workspace/NOTES.md','a').write('stage3 done: bulk qty>=100 x0.90, comma thousands in format_money.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])