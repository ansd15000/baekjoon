import sys

while(True):
    a, b= map(int, sys.stdin.readline().split())
    if not (0 <= a < 10 and 0 <= b < 10): continue
    if a == 0 and b == 0 : break
    print(a + b)


'''
import sys

def solution(a):
    pass

while(True):
    a = int(sys.stdin.readline().rstrip().split('\n'))
    if not :
        continue
    
    solution(a)

    break
'''