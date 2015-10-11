
def steep_array(l):
    c_total = 0
    for i in range(0, len(l)-2):
        c_total = l[i] + l[i+1]
        if l[i+2] <= c_total:
            return False
    return True

#
# 2 < 4 < 8 
#

def rsteep_array(l):
    if len(l) > 1:
        return l[0] < rsteep_array(l[1:])
    else:
        return 999999

def main():
    array = [2, 4, 8, 13]
    #try:
    #    array = input("Enter your array: ")
    #    array = array[:]
    #except:
    #    print 'Your array type must support slicing, ie it must be indexed :('
    
    print 'Using array:', array
    print rsteep_array(array)

if __name__ == '__main__':
    main()
