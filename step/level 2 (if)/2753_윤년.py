while(True):
    a = int(input())
    if a < 1 or a > 4000:
        continue
    result = (a % 4 == 0 and a % 100 != 0 or a % 400 == 0)
    print(int(result))
    break