src=open('/task/workspace/invoice/core.py').read()
src=src.replace("sub = sum((Decimal(l['qty']) * Decimal(l['unit_price']) for l in lines), Decimal('0'))","sub = sum((Decimal(l['qty']) * Decimal(l['unit_price']) * (Decimal('0.90') if l['qty'] >= 100 else 1) for l in lines), Decimal('0'))")
open('/task/workspace/invoice/core.py','w').write(src)
i=src.index('def format_money');print(src[i:])