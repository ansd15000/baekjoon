n = int(input())
a = sorted(map(int, input().split())) # 걸리는 시간 기준으로 정렬
result = 0
for i, j in enumerate(a):
    result += sum(a[:i + 1])
print(result)