p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("or q<=0: raise","or q<0: raise")
s=s.replace("        if not p.is_finite() or p<0: raise ValueError('negative price')\n","        if not p.is_finite() or p<0: raise ValueError('negative price')\n    lines=[l for l in lines if l['qty']>0]\n    if not lines: raise ValueError('all ignored')\n    return lines\n")
s=s.replace("    validate(lines)","    lines=validate(lines)")
open(p,'w').write(s)
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
print(s.count('lines=validate'),s.count('return lines'))