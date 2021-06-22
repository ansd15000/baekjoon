import sys

def solution(a):
    front = str(a)[-1] # 입력값의 1의자리 값
    end = str(sum(map(int, str(a))))[-1] # 더한 값의 1의자리 값
    return int(front + end)

while(True):
    a = int(sys.stdin.readline().rstrip())
    if not 0 <= a <= 99: continue
    
    value = solution(a)
    result = 1
    while value != a:
        value = solution(value)
        result += 1
    print(result)
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