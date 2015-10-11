
def steps(n):
    steps = 0
    for i in range(0, n):
        steps += 1
        for j in range(0, n):
            pos = n - j
            if steps - pos >= 0:
                print '#',
            else:
                print ' ',

        print ''   

def main():
    n = raw_input("n: ") 
    try:
        n = int(n)
    except:
        print "Enter a real integer"
    steps(n)

if __name__ == '__main__':
    main()
