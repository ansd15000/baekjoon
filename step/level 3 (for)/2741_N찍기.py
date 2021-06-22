import sys

def solution(a):
    for i in range(1, a + 1):
        print(i)
    # print( '\n'.join(map(str, range(1, a + 1))) ) # 이런 방식도 있대
    pass

while(True):
    a = int(sys.stdin.readline().rstrip())
    if not 1 <= a <= 100000:
        continue
    
    solution(a)

    break

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