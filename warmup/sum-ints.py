
def isum(l):
    total = 0
    for elm in l:
        total += elm
    return total

def rsum(l):
    if len(l) > 0:
        return l[0] + rsum(l[1:])
    return 0

ar = [12, 25, 30, 10, 14]

print ar, '=\t', isum(ar)
print ar, '=\t', rsum(ar)
