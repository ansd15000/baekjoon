def solution(n):
    for i in range(1, 10):
        print(f'{n} * {i} = {n * i}')
    pass

while(True):
    n = int(input())
    if not 1 <= n <= 9:
        continue
    
    solution(n)

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