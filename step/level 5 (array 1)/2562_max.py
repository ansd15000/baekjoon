# 갯수 제한이 없을때 어떻게 처리하지?
import sys

a = [int(sys.stdin.readline().rstrip()) for _ in range(9) ]
print(max(a))
print(a.index(max(a)) + 1)

'''
import sys

def solution(a):
    
    pass

while(True):
    a = int(sys.stdin.readline().rstrip())
    if not 0 <= a <= 99: continue
    break
'''