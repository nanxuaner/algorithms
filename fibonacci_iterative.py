def fibNum(n):
    if n == 0 or n == 1:
        return 1

    f = [1,1]
    # list to save numbers
    # scope
    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
        print "calculate fib %d, the result is %d" % (i, f[i])

    return f[n]

print fibNum(5)