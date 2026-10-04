import json,subprocess,sys
p='/task/workspace/invoice/core.py'
s=open(p).read().replace("rate=Decimal(0)","rate=Decimal('0.10')")
s+='''
PFX={'NZD':'NZ$','AUD':'A$','USD':'US$'}
def format_money(amount, currency):
    if currency not in PFX: raise ValueError('currency')
    a=r2(Decimal(str(amount)))
    sign='-' if a<0 else ''
    return sign+PFX[currency]+str(abs(a))
'''
open(p,'w').write(s)
open('/task/workspace/invoice/__init__.py','w').write('from .core import compute_invoice, format_money\n')
r=subprocess.run([sys.executable,'-m','unittest','discover','-s','/task/fixtures/current-tests'],cwd='/task/workspace',capture_output=True,text=True);print(r.stderr[-1500:])
c={'format':'clm-context/v1','entries':[{'id':'n1','role':'note','body':'Stage1 in invoice/core.py: line round half-up, subtotal, tier discount gold5%/silver2%, ValueError on empty/bad qty/neg price. Outputs str 2dp. Stage2: tax 10% on (sub-disc); format_money(amount,currency) NZ$/A$/US$, -prefix for neg, else ValueError. Exported in __init__.'}]}
json.dump(c,open('/task/workspace/context.json','w'))