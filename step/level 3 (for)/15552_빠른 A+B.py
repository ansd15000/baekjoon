# input 보다 빠른 sys.stdin.readline 
# 기본적으로 개행문자가 포함되기 때문에 rstrip으로 맨뒤 개행문자 제거해줌
import sys

while(True):
    T = int(sys.stdin.readline().rstrip()) 
    if not 0 < T < 1000001: continue

    loop = 0
    while(loop != T):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        if not (1 <= a <= 1000 and 1 <= b <= 1000) : continue
        print(a + b)
        loop += 1
    break
'''
def solution():
    pass

while(True):
    x = int(input())
    y = int(input())
    if not :
        continue
    
    solution()

    break
'''