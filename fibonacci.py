# recursive
def fibNum(n):
    if n == 0 or n == 1:
        return 1

    value = fibNum(n - 1) + fibNum(n - 2)

    return value

print fibNum(0)
print fibNum(1)
print fibNum(2)
print fibNum(3)
print fibNum(4)
print fibNum(5)