import sympy as sp
import numpy as np

l,lp,r = sp.symbols('l l^\\prime r', real=True)
eq1 = sp.Eq(4,lp/l)
eq2 = sp.Eq(1/l + 1/lp, 2/r)
sol = sp.solve([eq1, eq2], (l, lp))