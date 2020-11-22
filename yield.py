def fun():
    x = 0
    while True:
        x += 1
        yield x

x = fun()

for i in range(30):
    print next(x)
