import sympy as sp
import numpy as np

l1p,l,f1p,lp,fp,f2p = sp.symbols('l_1^\\prime l f_1^\\prime l^\\prime f^\\prime f_2^\\prime')
eq1 = sp.Eq(-1, l1p/l)
eq2 = sp.Eq(1/l1p - 1/l, 1/f1p)
eq3 = sp.Eq(-3/4, lp/l)
eq4 = sp.Eq(1/lp - 1/l, 1/fp)
eq5 = sp.Eq(lp, l1p - 20)
eq6 = sp.Eq(1/fp, 1/f1p + 1/f2p)
solutions = sp.solve([eq1, eq2, eq3, eq4, eq5, eq6], (l1p, f1p, lp, fp, f2p, l))
print(solutions)