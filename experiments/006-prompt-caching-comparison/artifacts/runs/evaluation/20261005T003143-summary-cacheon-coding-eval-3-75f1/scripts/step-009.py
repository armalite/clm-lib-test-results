src=open('/task/workspace/invoice/core.py').read()
src=src.replace("return sign + PREFIX[currency] + str(abs(a))","return sign + PREFIX[currency] + '{:,.2f}'.format(abs(a))")
open('/task/workspace/invoice/core.py','w').write(src)
open('/task/workspace/NOTES.md','a').write('Stage3 done: qty>=100 line*0.90; format_money comma thousands.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])