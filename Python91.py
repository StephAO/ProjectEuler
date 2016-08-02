# did with Miguel Aroca-Ouellette

count = 0

n = 50

for x1 in xrange(n+1):
    print x1
    for y1 in xrange(n+1):
        for x2 in xrange(n+1):
            for y2 in xrange(n+1):
                if (y1 == 0 and y2 == 0) or (x1 == 0 and y1 == 0) or (x2 == 0 and y2 == 0):
                    continue
                if (y1 != 0 and y2 != 0) and (float(x1)/float(y1) == float(x2)/float(y2)):
                    continue
                if y1 == 0 and x2 == 0 and x1 > 0 and y2 > 0:
                    count += 1
                    continue
                if 2*y1*(y1 - y2) + 2* x1*(x1 - x2) == 0:
                    count += 1
print count