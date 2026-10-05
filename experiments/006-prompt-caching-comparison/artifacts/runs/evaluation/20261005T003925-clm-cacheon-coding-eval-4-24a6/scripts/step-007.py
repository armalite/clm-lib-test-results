p='/task/workspace/invoice/core.py'
s=open(p).read()
s=s.replace("""        if q>=100:
            a*=Decimal('0.90')""","""        if q>=200:
            a*=Decimal('0.88')
        elif q>=50:
            a*=Decimal('0.95')""")
s=s.replace("""def format_money(amount, currency):
    raise NotImplementedError""","""PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}

def format_money(amount, currency):
    if currency not in PFX:
        raise ValueError('bad currency')
    d=r2(Decimal(str(amount)))
    sign='-' if d<0 else ''
    return sign+PFX[currency]+str(abs(d))""")
open(p,'w').write(s)
import subprocess,sys,json
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True)
print(r.stderr[-2000:])
n='Stage1: line=qty*price, round each line half-up; disc=r2(sub*tier); tax=r2((sub-disc)*rate); total. Stage2: tax 10% all; ValueError on empty lines/qty not pos int/negative price; tiers platinum10 gold7 silver3. Stage3: bulk qty>=200 x0.88 elif >=50 x0.95; format_money NZ$/A$/US$, 2dp, -prefix for negative, else ValueError. All in invoice/core.py (r2,TIER,TAX,PFX). Stage3 implemented; next: advance.'
json.dump({'format':'clm-context/v1','entries':[{'id':'sum1','role':'summary','body':n}]},open('/task/workspace/context.json','w'))