
def contains(elm, l):
    if not l: return False
    else: return l[0] == elm or contains(elm, l[1:])

print contains(2, [4,5,6,4,3,5,6,5,6,3,4,5,6,7,3,2,3,4,5,6,6,4])
