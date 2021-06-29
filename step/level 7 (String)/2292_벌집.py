import sys
# 커지는분기 꼭짓점
# 1 7 19 37 61
#  6 12 18 24  단위(6배수)

## 수학식쓰는거랑 차이가 없음 우와~
N = int(sys.stdin.readline().rstrip())
res = 1
for i in range(1000000001):
    res += (6 *i)
    
    if res >= N :
        print(i+ 1)
        break
    # print(f'{res:3d} 이하 {i+ 1:3d} 번방')
    
# 성한이가 수학적으로 푼 코드
# import sys, math
# N = int(sys.stdin.readline().rstrip())
# a = (N -1)/3
# b = math.ceil(math.sqrt(a)) #하고 값 올림
# if N == 1 : print(1)
# else: print(math.ceil(math.sqrt(a + b))) #하고 값 올림
