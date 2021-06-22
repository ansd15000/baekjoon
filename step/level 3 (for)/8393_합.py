def solution(x):
    # res = 0
    # for i in range(1, x + 1):
    #     res += i
    # print(res) # 일방적
    
    # 수학식으로 연산. 2제곱 + x 의 몫으로 계산
    print( (x ** 2 + x) // 2 )
    pass

while(True):
    x = int(input())
    if not 1 <= x <= 10000:
        continue
    
    solution(x)

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