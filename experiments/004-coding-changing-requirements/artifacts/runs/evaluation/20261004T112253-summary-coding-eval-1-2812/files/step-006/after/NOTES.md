S1: rounding per line half-up, tax 10%, bulk qty>=100 x0.90. impl in invoice/core.py
S2: validation (empty, qty pos int, price>=0 ValueError); bulk CHANGED: >=200 x0.88, >=50 x0.95.
S3: tier disc gold5 silver2; rounding CHANGED: exact, then half-even on sub/disc/tax.
