# 타입에 맞게 함수 생성하기
from functools import reduce # 굳이 누적값 더하는 reduce 쓸 필요가 없음

# def solve(a: list) -> int:
#     return reduce(lambda x, y : x + y, a)

def solve(a: list) -> int: return sum(a)
