import subprocess,sys,re
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("TIER={'gold':Decimal('0.05'),'silver':Decimal('0.02')}","TIER={'platinum':Decimal('0.10'),'gold':Decimal('0.07'),'silver':Decimal('0.03')}")
s=s.replace("    return Decimal(0)\n","    return Decimal('0.10')\n",1)
s=s.replace("    sub=Decimal(0)\n","""    if not lines: raise ValueError('empty')
    for l in lines:
        q=l.get('qty')
        if not isinstance(q,int) or isinstance(q,bool) or q<=0: raise ValueError('qty')
        try: up=Decimal(str(l['unit_price']))
        except Exception: raise ValueError('price')
        if not up.is_finite() or up<0: raise ValueError('price')
    sub=Decimal(0)
""",1)
open(p,'w').write(s)
open('/task/workspace/NOTES.md','a').write('stage2 done: tax10%, validation, tiers plat10/gold7/silver3\n')
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])