# 유클리드 호제법.. 두 수중 큰 수를 나머지연산으로 0이 될때까지 진행. 그 값이 최대공약수니까 그걸활용함
n = int(input())
for i in range(n):
    A, B = map(int, input().split())
    a, b = A, B
    while b != 0:
        a %= b
        a, b = b, a
    print((A * B) // a)
