import math

file = open("p099_base_exp.txt", 'r')

separated_primes = []
largest_num = 0
index = -1
for i in xrange(1000):
    line = file.readline()
    base, exponent = map(lambda x : int(x), line.split(','))
    if math.log(base)*exponent > largest_num:
        print i
        largest_num = math.log(base)*exponent
        index = i
print index+1
