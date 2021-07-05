# 왜 인덱스 런타임 에러?
# a, b = map(int, input().split())
# z = set([i for i in range(2, a) if a % i == 0])
# x = set([i for i in range(2, b) if b % i == 0])
# res1 = sorted(list(x.intersection(z)))[-1] # 교집합
# print(res1)             # 최대공약수
# print((a * b) // res1)  # 최소공배수

# 유클리드 호제법
A, B = map(int, input().split())
a, b = A, B
while b != 0:
    a %= b
    a,b = b, a # 스왑이 그냥 되네
print(a)
print(A*B // a)