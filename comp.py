import sympy as sp
import numpy as np

l1,l1p,fp = sp.symbols('l_1 l_1^\\prime f^\\prime', real=True)
eq1 = sp.Eq(l1p - l1, 900)
eq2 = sp.Eq(1/l1p - 1/l1, 1/fp)
l = sp.symbols('l', real=True)
eq3 = sp.Eq(1/(l1p - l) - 1/(l1 - l), 1/fp)
eq4 = sp.Eq((l1p)/(l1), -(l1p - l)/(l1 - l)/4)
sol = sp.solve([eq1, eq2, eq3, eq4], (l1, l1p, fp,l))