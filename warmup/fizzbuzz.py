n = raw_input("lenght: ")
n = int(n) + 1

for i in range(1, n):
    fizz = (i % 5 == 0)
    buzz = (i % 7 == 0)
    if fizz and buzz:
        print "fizzbuzz"
    elif fizz:
        print "fizz"
    elif buzz:
        print "buzz"
    else:
        print i
