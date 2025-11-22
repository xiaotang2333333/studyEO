import sympy as sp
import numpy as np

f1p,f2p = sp.symbols(" f_1^{\\prime} f_2^{\\prime}",real = True)
L = 65
lkp = 50
d = 15
fp = 35
h1 = 100
#define temp variables
h2 = sp.symbols(" h_2",real = True)
eq1 = sp.Eq(h1*(1 - d/f1p), h2)
eq2 = sp.Eq(h2/lkp, h1/fp)
eq3 = sp.Eq(1/fp,1/f1p + 1/f2p - d/(f1p*f2p))
sol = sp.solve([eq1, eq2, eq3], (f1p, f2p, h2))