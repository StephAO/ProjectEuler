import itertools as it
import time

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    # print '\t',f
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f +=6
  return True

def primes1(n):
    """ Returns  a list of primes < n """
    sieve = [True] * (n/2)
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i/2]:
            sieve[i*i/2::i] = [False] * ((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1,n/2) if sieve[i]]

def get_digits(n):
    digits = []
    while n > 0:
        digits.insert(0,n%10)
        n = int(n/10)
    return digits

def get_hash(star_loc, digits):
    sh = []
    for i in xrange(len(digits)):
        if i in star_loc:
            sh.append('*')
        else:
            sh.append(digits[i])
    return sh

def star_hash_to_int(star_hash, d):
    integer = 0
    multiplier = 1
    num_digits = len(star_hash)

    for i in xrange(num_digits):
        digit = star_hash[num_digits-i-1]
        if digit == '*':
            digit = d
        # print star_hash, " = integer: ", integer, " + ", digit, "*", multiplier
        integer += digit*multiplier
        multiplier *= 10
    return integer

def n_size_family(star_hash, primes, n=8):
    count = 0
    smallest = None
    digits = xrange(1,10) if star_hash[0] == '*' else xrange(10)
    for i in digits:
        new_num = star_hash_to_int(star_hash, i)
        if new_num in primes:
            if smallest is None:
                smallest = new_num
            count += 1
        if count+(9-i) < n:
            return False, 0, count
    return (count >= n), smallest, count

def main():
    stime = time.time()
    already_checked = {}
    not_found = True
    i = 0
    primes_list = primes1(1000000)
    primes = dict((p,0) for p in primes_list)
    while not_found:

        if i in primes:
            # print i
            digits = get_digits(i)
            num_digits = len(get_digits(i))
            for num_stars in xrange(1,num_digits):
                if not not_found:
                    break
                star_locations = list(it.combinations(range(num_digits), num_stars))
                for star_loc in star_locations:
                    star_hash = get_hash(star_loc, digits)
                    if tuple(star_hash) in already_checked:
                        # print '-'
                        continue
                    already_checked[tuple(star_hash)] = True
                    # print digits, i, star_loc, star_hash
                    valid, smallest, count = n_size_family(star_hash, primes, n=8)
                    # print count, valid, smallest
                    if valid:
                        print smallest, star_hash
                        not_found = False
                        break
        i += 1
    print "time taken:", time.time() - stime

if __name__ == "__main__":
    main()
