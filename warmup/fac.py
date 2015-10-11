def fac(n):
    n = abs(n)
    total = 1
    while n > 1:
        total = total * n
        n = n -1
    return total

def rfac(n):
    n = abs(n)
    if n <= 1:
        return 1
    else:
        return n * rfac(n-1)

print '4! =', fac(4)
print '6! =', rfac(6)
print '10! =', fac(10)
print '11! =', rfac(11)
