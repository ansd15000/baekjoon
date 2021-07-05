#       약수    , 배수      , 둘다아님
res = ['factor','multiple','neither']
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0 : break

    if b % a == 0 : print(res[0]) 
    elif a % b == 0 : print(res[1])
    else: print(res[2])
