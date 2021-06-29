Fibonacci = [0, 1]
a = int(input())
if a < 2: print(Fibonacci[a])
else:
    for _ in range(2, a + 1):
        temp = Fibonacci[0]
        Fibonacci[0] = Fibonacci[1]
        Fibonacci[1] = temp + Fibonacci[1]
    print(Fibonacci[-1])