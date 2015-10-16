import math

def get_perm(l):
    
    if len(l) == 1:
        return [0]
    elif len(l) == 2:
        return [[0, 1], [1, 0]] 
        
    new = []
    for i in range(0, len(l)):
        new.append([i] + get_perm(l[:i] + l[i+1:]))
    return new
            
s = 'asdfghi'
perms = get_perm(s)

def print_perms(perms, s):
    for i in perms:
        if i not type(l):
            print s[i]
        else:
