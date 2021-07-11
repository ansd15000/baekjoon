from sys import stdin
a = sorted([list(map(int, stdin.readline().split())) for _ in range(int(input()))])
for i, j in a: 
    print(i, j)

# 2차원 리스트도 그냥 소트하면 오름차순으로 정렬됨... 이야 이건 몰랐네