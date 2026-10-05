p='/task/workspace/invoice/core.py';s=open(p).read()
s=s.replace('TIER = {"gold": Decimal("0.05"), "silver": Decimal("0.02")}','TIER = {"platinum": Decimal("0.10"), "gold": Decimal("0.07"), "silver": Decimal("0.03")}')
s=s.replace('    rate = Decimal("0")','    rate = Decimal("0.10")')
s=s.replace('    sub = Decimal("0")\n','''    if not lines:\n        raise ValueError("empty lines")\n    for l in lines:\n        q = l.get("qty")\n        if not isinstance(q, int) or isinstance(q, bool) or q <= 0:\n            raise ValueError("bad qty")\n        if Decimal(str(l["unit_price"])) < 0:\n            raise ValueError("negative price")\n    sub = Decimal("0")\n''')
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage2 done: tax 10%, validation, tiers plat10 gold7 silver3.\n')
import subprocess,sys
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2000:])