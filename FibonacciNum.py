# def fibonacciNum(n):
#     if n == 0 or n == 1:
#         return 1
#
#     f = [1, 1]
#     for i in range(2, n+1):
#         f.append(f[i-1] + f[i-2])
#         print ("calculate fib %d, the result is %d" % (i, f[i]))
#
#     return f[n]
#
# t = fibonacciNum(10)
# print (t)
#
# def fibonacciNum(n):
#     if n == 0 or n == 1:
#         return 1
#
#     f = [1, 1]
#     for i in range(2, n+1):
#         f.append(f[i-1] + f[i-2])
#         print ("calculate fib %d, the result is %d." % (i, f[i]))
#
#     return f[n]
#
# t = fibonacciNum(11)
# print t

# def fibnacciNum(n):
#     if n == 0 or n == 1:
#         return 1
#
#     f = [1, 1]
#
#     for i in range(2, n+1):
#         f.append(f[i-1] + f[i-2])
#         print "calculate fib %d, the result is %d" % (i, f[i])
#         print f
#
#     return f[n]
#
# t = fibnacciNum(11)
# print t
#
# def fibnacciNum(n):
#     if n == 0 or n == 1:
#         return 1
#
#     f = [1, 1]
#
#     for i in range(2, n+1):
#         f.append(f[i-1] + f[i-2])
#         print ("calculate fib %d, the result is %d" %(i, f[i]))
#         print f
#
#     return f[n]
#
# fibnacciNum(6)

def fibnacciNum(n):
    if n == 0 or n == 1:
        print ("1")
        return 1

    f = [1, 1]

    for i in range(2, n+1):
        f.append(f[i-1] + f[i-2])
        print ("calculate fib %d, the result is %d" %(i, f[i]))
        print f



fibnacciNum(2)