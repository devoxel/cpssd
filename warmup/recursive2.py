def seqlen(l):
    if not l:    
        return 0
    else:
        return 1 + seqlen(l[1:])

def max_value(l):
	if len(l) == 0:
		return 0
	elif len(l) == 1:
		return l[0]
	prev = max_value(l[1:])
	if prev > l[0]:
		return prev
	else:
		return l[0]

def steep_array(l):
	if len(l) <= 2:
		return True
	else:
		stp =  l[-1] > l[-2] + l[-3]
		return steep_array(l[2:]) and stp

def optimal_steep_array(l, i):
	if i >= len(l)-2:
		return True
	else:
		stp = l[len(l)-i] > l[len(l)-(i+1)] + l[len(l)-(i+2)]
		return optimal_steep_array(l, i+3) and stp

array = [1, 2, 7, 10]
steep = steep_array(array)

print 'steep?: ', array, steep

array = [-20, -10, 10, 100]
steep = steep_array(array)

print 'steep?: ', array, steep

array = [-20, -10, 100, 10]
steep = optimal_steep_array(array, 1)

print 'steep?: ', array, steep
