# l = sorted([int(input()) for _ in range(int(input()))])

# def m(a, b):
#     while b != 0:
#         a, b = b, a%b
#     return a


# l = [m(l[i], l[i+1]) for i in range(len(l)-1)]
# print(l)


# a = [5, 17, 23, 14, 83]
# a = [6,34,38]
# b = list(set(map(lambda x : x % a[0], a[1:] )))
# print(' '.join([str(i) for i in b if len(set([j % i for j in a])) == 1]))

# 왜 틀렸는지 모르겟어. 사실 수학식을 몰라서 그래.. 시발아
# a = sorted([int(input()) for _ in range(int(input()))])
# b = sorted(set(map(lambda x : x % a[0], a[1:] )))
# if b[0] == 0 : b = b[1:]
# a = [str(i) for i in b if len(set([j % i for j in a])) == 1]
# if len(a) > 0: 
#     print(' '.join(a))

# def test(l:list, x):
#     for i in l:
#         print(i % x, end=' ')
#     print()

# for i in b:
#     test(a, i)

'==========================================================='
# 틀린이유... 나머지가 같은 값들을 출력해야하니까.. 수학식으로 따져서 처리해야하는거셈. 수학 모른다구 ㅠ

def gcd(x,y):
    mod = x % y
    while mod >0:
        x = y
        y = mod
        mod = x % y
    return y

#약수 리스트를 구해주는 함수
def div(x):
    div_list = [x]
    for i in range(2, int(x**(1/2) + 1)):
        if x % i == 0:
            div_list.append(i)
            if x//i != i:
                div_list.append(x//i) 
    div_list.sort()
    return div_list 
    

#입력함수
N = int(input())
freight = []
for _ in range(N):
    freight.append(int(input()))
freight.sort(reverse = True)


#화물들의 차이 입력
freight_diff = []
for i in range(len(freight)-1):
    freight_diff.append(freight[i] - freight[i+1])

#화물들의 차이를 최대공약수 함수를 이용해 구해주기
if len(freight_diff) == 1:
    answer = freight_diff[0]
elif len(freight_diff) == 2:
    answer = gcd(freight_diff[0], freight_diff[1])
else:
    answer = freight_diff[0]
    for i in range(1, len(freight_diff)):
        answer = gcd(answer, freight_diff[i]) 

print(answer)
#구한 최대공약수의 모든 약수 출력
for i in div(answer):
    print(i, end = ' ')

'''
from math import sqrt, floor, gcd
 
N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
diff = []
ans = set()
for i in range(N):
    for j in range(i+1, N):
        diff.append((arr[i]-arr[j]) if arr[i]>arr[j] else (arr[j]-arr[i]))
diff.sort()
 
if len(diff) > 1:
    temp = gcd(diff[0], diff[1])
    for i in range(2, N):
        temp = gcd(temp, diff[i])
else:
    temp = diff[0]
 
for i in reversed(range(1, int(sqrt(temp)+1))):
    #print(i)
    if temp % i == 0:
        ans.add(i)
        ans.add(temp//i)    
ans = list(ans)
ans.sort()
for a in ans[1:]:
    print(a, end=' ')
'''