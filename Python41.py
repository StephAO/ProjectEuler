import prime_stuff as ps
import itertools as it
import time

stime = time.clock()

found = False
for n in xrange(7,0,-1):
    for comb in it.permutations(xrange(n,0,-1), n):
        num = int(''.join(map(str,comb)))
        print num
        if ps.is_prime(num):
            print num
            found = True
            break
    if found:
        break

print 'time taken:', time.clock() - stime