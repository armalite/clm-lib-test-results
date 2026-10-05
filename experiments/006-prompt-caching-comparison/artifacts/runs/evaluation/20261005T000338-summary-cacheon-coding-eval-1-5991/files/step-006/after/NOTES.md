Stage1: line round half up, bulk qty>=100 x0.90, tax 10%, discount 0.
Stage2: validation (empty, qty pos int, price>=0 ValueError); bulk >=200 x0.88, >=50 x0.95.
Stage3: tier discount gold5 silver2; no line rounding, exact then half-even round s,d,t; total from rounded.
