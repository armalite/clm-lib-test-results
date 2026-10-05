Stage1: line round half up, bulk qty>=100 x0.90, tax 10% all, discount 0.
Stage2: validation ValueError (empty, qty not pos int, neg price); bulk >=200 x0.88, >=50 x0.95 (replaces 100 rule).
Stage3: tier gold5 silver2; no line rounding, exact then half-even round s,d,t.
