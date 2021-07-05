# 블랙잭은 안해봤지만 세개를 무조건 뽑아야 하는 룰이 있는거같아.
# n, m = map(int, input().split())
# a = sorted(map(int, input().split()))[::-1]
# res = 0
# # loop = int(n / 2)
# for i in range(n):
#     chk = 0
#     cnt = 0
#     for j in a[i:]:
#         if cnt == 3: break
#         if m >= chk + j:
#             cnt += 1
#             chk += j
#     if chk > res and cnt == 3: 
#         res = chk
# print(res)

# iterator 타입 데이터에 대한... 특정 반복자를 처리시키는 내장라이브러리
# from itertools import combinations
# n, m = map(int, input().split())
# a = list(map(int, input().split()))
# result = 0
# for i in list(combinations(a, 3)):
#     if result < sum(i) <= m :
#         result = sum(i)
# print(result)

# 라이브러리를 안쓰는게 알고리즘 풀이에 도움이 될 테니까 해봤어.. 절반정도 베꼈지만..
import sys
n, m = map(int, input().split())
a = list(reversed(sorted(map(int, input().split()))))
l = set()
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            b = a[i] + a[j] + a[k]
            if b == m : 
                print(m)
                sys.exit() # 여기서 걍 반복문 안빠져나가고 코드 종료시키기 위함
            else:
                if b < m:
                    l.add(b)
                    break
print(max(l))