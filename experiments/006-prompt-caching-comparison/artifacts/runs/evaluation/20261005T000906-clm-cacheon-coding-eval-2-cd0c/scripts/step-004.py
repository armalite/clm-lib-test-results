import subprocess,sys,json
p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("rate=Decimal('0')","rate=Decimal('0.10')")
i=s.index('def format_money')
s=s[:i]+'''PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PFX:
        raise ValueError('currency')
    a=_r(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+PFX[currency]+str(abs(a))
'''
open(p,'w').write(s)
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-2500:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1+2 in invoice/core.py: compute_invoice (half-up line rounding via _r, tier discount gold5%/silver2% TIER dict, validation, tax 10% on sub-disc, returns str fields); format_money with PFX dict NZ$/A$/US$, -before prefix, ValueError unknown. Next: run tests, advance to stage 3.'}]}
json.dump(c,open('/task/workspace/context.json','w'))