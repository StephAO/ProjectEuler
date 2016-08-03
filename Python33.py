import copy as cp
import fractions
from decimal import Decimal


def numb(n):
    return float(n[0]*10 + n[1])

fractions_ = []
for i in xrange(10,100):
    for j in xrange(i+1,100):
        a_dig = [int(d) for d in list(str(i))]
        b_dig = [int(d) for d in list(str(j))]
        for d in a_dig:
            if d in b_dig and d != 0:
                new_a_dig = cp.copy(a_dig)
                new_b_dig = cp.copy(b_dig)
                new_a_dig.remove(d)
                new_b_dig.remove(d)

                if new_b_dig[0] == 0:
                    continue
                
                if float(new_a_dig[0])/float(new_b_dig[0]) == numb(a_dig)/numb(b_dig):
                    fractions_.append((numb(a_dig), numb(b_dig)))

product = 1
for f in fractions_:
    product *= (f[0]/f[1])
print product



