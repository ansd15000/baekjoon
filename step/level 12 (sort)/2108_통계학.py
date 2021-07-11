import sys
from collections import Counter # 리스트에서 요소당 빈도값을 튜플로 묶어 리스트로 반환해주는 라이브러리

n = int(sys.stdin.readline())
a = sorted([int(sys.stdin.readline()) for i in range(n)])
val = Counter(a).most_common() # 최빈값
def mode():
    if len(val) > 1: 
        if val[0][1] == val[1][1] :
            print(val[1][0])
        else:
            print(val[0][0])
    else:
        print(val[0][0])

print(round(sum(a) / n))
print(a[n//2])
mode()
print(a[-1] - a[0])

# 숭인점 이디야
# 미들 토일 12시 17시
# 1시간 정도 걸림

