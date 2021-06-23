def d(a) :
    b = str(a)
    for i in b:
        a += int(i) # 각 자리수 더한 값 
    return a

result = {d(i) for i in range(1, 10001)} # 쓸데없는 연산이 조금 더 들어감..
result = sorted(set(range(1, 10001)).difference(result))
for i in result:
    print(i)

'''
# 개신기하네ㅋㅋㅋ
a = [True]*20000
for i in range(10):
    for j in range(10):
        for k in range(10):
            for l in range(10):
                a[1001*i+101*j+11*k+2*l] = False
for i in range(10000):
    if a[i] == True:
        print(i)
'''