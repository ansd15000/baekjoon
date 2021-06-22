def solution(h, m):
    m -= 45
    if m < 0:
        h -= 1
        m += 60
        if h < 0: h += 24

    return h, m

while(True):
    h, m = map(int, input().split())
    if not 0 <= h <= 23 and 0 <= m <= 59:
        continue
    h, m = solution(h, m)
    print(h, m)
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
