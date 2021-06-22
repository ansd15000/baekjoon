# 더 좋은 방법이 있었을까... 

while(True):
    x = int(input())
    y = int(input())
    if not -1000 <= x <= 1000 and -1000 <= y <= 1000:
        continue
    
    if x > 0 and y > 0: print(1)
    elif x < 0 and y > 0: print(2)
    elif x < 0 and y < 0: print(3)
    else: print(4)

    break