T = int(input())
for i in range(T):  # 반복입력받을 총 개수
    while(True):    # 제약사항을 위한 반복
        a,b = map(int, input().split())
        if not (0 < a < 10 and 0 < b < 10):
            continue
        print(a + b)
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