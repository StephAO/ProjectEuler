import time

stime = time.clock()

per_count = {}
for i in xrange(1,998):
    for j in xrange(i,999):
        if i + j > 1000:
            break
        for k in xrange(j,1000):
            if i + j + k > 1000:
                break
            if i**2 + j**2 == k**2:
                count = per_count.get((i+j+k))
                if count is None:
                    per_count[(i+j+k)] = 0
                per_count[(i+j+k)] += 1

largest = 0
sol = None
for key in per_count:
    if per_count[key] > largest:
        largest = per_count[key]
        sol = key
print sol
print "time taken:", time.clock() - stime