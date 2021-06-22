import sys

# 멈추는 조건이 따로 없어서 걍 이래함.
while(True):
    try:
        a, b= map(int, sys.stdin.readline().split())
        if not (0 < a < 10 and 0 < b < 10): continue
        print(a + b)
    except:
        break

# 보통 입력값에 대한 처리는 이래해서 속도가 빠르게 처리됨. 근데 명령이 끝나진 않음.
# for line in sys.stdin: print(sum(map(int, line.split())))

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