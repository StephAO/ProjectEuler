
num_string = ''
for i in xrange(1000000):
    num_string += str(i)

print int(num_string[1])*int(num_string[10])*int(num_string[100])*int(num_string[1000])*int(num_string[10000])*int(num_string[100000])*int(num_string[1000000])