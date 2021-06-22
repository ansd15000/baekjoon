def solution(a):
    # join이 리스트를 문자열로 병합해줌. \n 을 각각 추가해서
    a = '\n'.join(map(str, range(a,0,-1)))
    print(a)
    pass

while(True):
    a = int(input())
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