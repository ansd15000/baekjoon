# sorted로 때려박기
# print( '\n'.join(map(str, sorted([int(input()) for i in range(int(input())) ]))) )

# 공부의 정석
n = int(input())
a = [int(input()) for _ in range(n)]
# 5 2 3 4 1
for i in range(n):
    for j in range(i+1, n):
        if a[i] >= a[j]: a[i], a[j] = a[j], a[i]
    print(a[i])

