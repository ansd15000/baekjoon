n = int(input())
a = list(map(int, input().split())) # 마을당 거리
b = list(map(int, input().split())) # 주유소 리터당 가격

# 걍... 최소값 하나 두고.. 순차로 곱하면 되는거엿음...
# 왜 어렵게 생각하는거야?
res= 0
m = b[0]
for i in range(len(b) - 1):
    if b[i] < m: m = b[i]
    res += m * a[i]
print(res)