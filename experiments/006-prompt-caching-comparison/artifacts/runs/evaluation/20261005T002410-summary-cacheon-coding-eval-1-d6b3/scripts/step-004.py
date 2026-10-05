p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("""    subtotal=Decimal('0')
    for l in lines:""","""    if not lines:
        raise ValueError('empty lines')
    for l in lines:
        q=l.get('qty')
        if isinstance(q,bool) or not isinstance(q,int) or q<=0:
            raise ValueError('bad qty')
        if Decimal(str(l['unit_price']))<0:
            raise ValueError('negative price')
    subtotal=Decimal('0')
    for l in lines:""")
s=s.replace("""        if l['qty']>=100:
            amt*=Decimal('0.90')""","""        if l['qty']>=200:
            amt*=Decimal('0.88')
        elif l['qty']>=50:
            amt*=Decimal('0.95')""")
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('Stage2: validation ValueError (empty, qty not pos int, neg price); bulk >=200 x0.88, >=50 x0.95 (replaces 100 rule).\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])