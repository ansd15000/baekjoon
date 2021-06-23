import sys
ascdial = ['A', 'D', 'G', 'J', 'M', 'P', 'T', 'W', '['] # 아스키 Z값 다음이 [
a = sys.stdin.readline().rstrip()
result = 0
for i in a:
    for j in range(len(ascdial)):
        if i >= ascdial[j] and i < ascdial[j+1]:
            result += j
    result += 3 # 앞파벳이 할당되는 다이얼은 숫자2부터라 +1, 다이얼 위치당 +2 = 3
print(result)
