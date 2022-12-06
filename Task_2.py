import random
x = [random.randrange(-10, 10), random.randrange(-10, 10), random.randrange(-10, 10)]
for i in range(10):
    print((not(x[0] or x[1] or x[2])) == (not(x[0]) and not(x[1]) and not(x[2])))
