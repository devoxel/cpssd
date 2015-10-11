def countup(n, i=1):
    if i <= n:
        print i
        countup(n, i+1)

def readn(n='0'):
    if n != '-1':
        n = raw_input('n: ')
        print '\t' + n
        return readn(n)

def it_countup(n):
    print range(1, n+1)

def it_readn():
    while True:
        n = raw_input('n: ')
        print '\t' + n 
        if n == '-1':
            break

countup(3)
it_countup(3)

it_readn()
