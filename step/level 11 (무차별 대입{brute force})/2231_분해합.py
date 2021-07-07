# 0.9초 아슬아슬했다잉
a = int(input())
l = []
for i in range(a - 1, 0, -1):    
    result = i + sum(map(int, list(str(i))))
    if result == a :
        l.append(i)
    if int(a/2) > result : break
if len(l) == 0: print(0)
else: print(min(l))