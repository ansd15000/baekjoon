import sys
from functools import reduce

# 값 활용을 기준으로 생각했더니.. 시간이 2배가 걸리네 (100ms)
a = [int(sys.stdin.readline().rstrip()) for _ in range(3) ]
mul = reduce(lambda x, y : x * y, a) # 리스트 값 누적 계산
# result = [0 for _ in range(10)] # 0값 리스트에 갯수만큼 추가
# for i in str(mul):
#     result[int(i)] += 1
# print('\n'.join(map(str,result)))
result = list(map(int, str(mul)))
for i in range(10): print(result.count(i))


# 걍 수동으로 때려박고 성능중시는 이렇게. (68ms)
# a, b, c = int(input()), int(input()), int(input())
# d = list(map(int, str(a * b * c)))
# for i in range(10):
#     print(d.count(i))
