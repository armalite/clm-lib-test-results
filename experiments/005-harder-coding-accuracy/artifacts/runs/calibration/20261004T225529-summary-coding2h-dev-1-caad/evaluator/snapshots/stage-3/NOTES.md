stage1: rounding half up per line/discount/tax; validation; tax 10%. impl in core.py
stage2: tier disc gold5 silver2 on subtotal (rounded); bulk qty>=100 x0.90 before line round
stage3: shipping 7.50 if sub-disc<100 else 0, untaxed
