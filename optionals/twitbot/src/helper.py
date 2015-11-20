
def safe_get(l, index, default=None):
    if len(l) >= index+1 :
        if len(l[index]) > 0:
            return l[index]
    return default
