import sys

while(True):
    N = int(sys.stdin.readline().rstrip())
    if not 1 <= N <= 1000000: continue
    a = list(map(int, sys.stdin.readline().split())) # 리스트 제약조건은 잘 모르겟다..
    print(f'{min(a)} {max(a)}')
    break

'''
import sys

def solution(a):
    
    pass

while(True):
    a = int(sys.stdin.readline().rstrip())
    if not 0 <= a <= 99: continue
    break
'''
# 5
# 20 10 35 30 7