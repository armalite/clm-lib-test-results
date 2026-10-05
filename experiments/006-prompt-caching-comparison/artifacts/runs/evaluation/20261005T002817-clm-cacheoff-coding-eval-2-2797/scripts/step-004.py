import subprocess,sys,json
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace('Decimal(0))\n    return','Decimal("0.10"))\n    return')
s=s.replace('''def format_money(amount, currency):
    raise NotImplementedError''','''PFX={"NZD":"NZ$","AUD":"A$","USD":"US$"}
def format_money(amount, currency):
    if currency not in PFX: raise ValueError("currency")
    a=r(Decimal(str(amount)))
    return ("-" if a<0 else "")+PFX[currency]+str(abs(a))''')
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'core.py: r()=quantize half-up; RATES tier dict; compute_invoice validation+tier discount+tax via `t=r((sub-d)*Decimal("0.10"))`; format_money with PFX dict. Stage1 rules: line rounding, gold5/silver2, ValueError on empty/bad qty/neg price. Stage2: tax 10%, format_money NZ$/A$/US$, -prefix, else ValueError. Stage 2 done when tests pass; next: advance.'}]}
json.dump(c,open('/task/workspace/context.json','w'))