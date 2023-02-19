def fib_intervall(x):
    if x < 0:
        return -1
    (old, new) = (0, 1)
    while True:
        if new < x:
            (old, new) = (new, old + new)
        else:
            if new == x:
                new = old + new
            return (old, new)
while True:
    x = int(input("Your number: "))
    if x <= 0:
        break
    (lub, sup) = fib_intervall(x)
    print("Largest Fibonacci Number smaller than x: " + str(lub))
    print("Smallest Fibonacci Number larger than x: " + str(sup))
