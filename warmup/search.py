import sys

def search(l, n):
    for i in l:
        if n == i:
            print "It's here"
            return None
    print "Nope!"

def other_search(l, n):
    for i in l:
        if n == i:
            print "It's here"
            break
    else:
        print "Nope!"

if __name__ == '__main__':
    l = []
    try:
        for arg in sys.argv[2:]:
            l.append(int(arg))
        searching = int(sys.argv[1])
        search(l, searching)
        print 'doing it with the other thing'
        other_search(l, searching)
    except IndexError:
        print 'WHOOOPS!'
    except ValueError:
        print 'WHOOOPS!'
