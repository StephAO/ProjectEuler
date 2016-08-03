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

def concat_numbers(n_list):
    return int(''.join([str(n) for n in n_list]))

largest_num = 0
for i in xrange(10000):
    digits = [False]*9
    to_concat = []
    for j in xrange(1,9):
        to_concat.append(i*j)
        if not get_digits(i*j, digits):
            break
        if all(digits):
            number = concat_numbers(to_concat)
            if number > largest_num:
                largest_num = number
print largest_num
