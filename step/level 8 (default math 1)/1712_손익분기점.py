import sys
# 고정제조단가, 유동제조단가, 판매가
a, b, c = map(int, sys.stdin.readline().split())

# 판매가와 유동제조단가는 정비례. 그니까 걍 판매가에서 빼버림
if c - b <= 0 : print(-1)   # 이때 음수가 나오면 컽
else: print( (a // (c - b)) + 1)  # 몫으로 나눈 수에 +1 하면 최초 손익분기점 돌파