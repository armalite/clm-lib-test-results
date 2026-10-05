import subprocess,sys,json
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace('    t=r((sub-d)*Decimal("0.10"))','    t=Decimal("0.00") if customer.get("tax_exempt") is True else r((sub-d)*Decimal("0.10"))')
s=s.replace('PFX[currency]+str(abs(a))','PFX[currency]+"{:,.2f}".format(abs(a))')
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'All 4 stages implemented in core.py (stage4: tax_exempt is True -> tax 0.00; format_money comma thousands). If tests pass: final.'}]}
json.dump(c,open('/task/workspace/context.json','w'))