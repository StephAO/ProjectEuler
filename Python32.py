import time

def get_digits(n, digits):
    while n >= 1:
        d = n%10
        if d == 0:
            return False
        if digits[d-1]:
            return False
        else:
            digits[d-1] = True
        n = int(n/10)
    return True

stime = time.clock()
sum_ = 0
products = []
for i in xrange(2,200):
    if i%1000 == 0:
        print '---',i,'---'
    for j in xrange(i+1,2000):
        digits_used = [False]*9
        if not get_digits(i, digits_used): 
            continue
        if not get_digits(j, digits_used): 
            continue
        if not get_digits(i*j, digits_used): 
            continue
        if all(digits_used) and (i*j not in products):
            products.append(i*j)
            sum_ += i*j
print sum_

print 'time taken', time.clock() - stime