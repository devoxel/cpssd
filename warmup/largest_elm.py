
def ilargest(l):
    largest = 0
    for elm in l:
        if elm > largest:
            largest = elm
    return largest

def rlargest(l, largest=0):
    if len(l) > 0:
        if l[0] > largest:
            return rlargest(l[1:], l[0])
        return rlargest(l[1:], largest)
    return largest

ar = [12, 25, 30, 10, 14]

print ar, '=\t', ilargest(ar)
print ar, '=\t', rlargest(ar)

