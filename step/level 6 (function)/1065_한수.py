# 수열이란? 특정 규칙을 가진 수의 나열
# 등차수열? 인접한 수의 차이가 같은 수의 나열 ex) 1 3 5 ...
#   이때 간격 2를 '공차'. 첫번째 값 1을 '초항' 이라고 함. 
#   즉 위 예시는 공차가 2고 초항이 1인 등차수열이라고 표현한다.
#   1자리수 값들도 자기 자신을 공차로 갖는 등차수열이라 할 수 있다.

# 등차수열의 일반항 (위 등차수열을 기준)
# 공차가 2면 2n. 이때 n에 1을 넣었을때 초항 값이 나와야함.
# -> 2n - 1 다음과 같은 식으로 n번째에 있는 수열값을 확인가능

# 한수: 양의 정수 N의 각 자리수가 등차수열을 이루는 값 (ex: 888 이게 수열 8 8 8 과 동일함을 의미)
# ex) 130 의 경우 길이가 3인 1 3 0 수열로 판단. 공차확인이 안되니 등차수열 아님. 패스 
import sys
n = int(sys.stdin.readline().rstrip())
cnt = 100     # 반복 수
result = 99   # 한수 갯수

def getChasu(a :str, b: str) -> int:
    return int(b) - int(a) 

if n // 1 < 100 :   # 두자리 수열은 그 만큼 한수가 있음
    print(n//1)
else :              # 3자리수 이상 수열일떄
    while cnt <= n :
        Hansu = True
        __n = str(cnt)
        chasu = getChasu(__n[0], __n[1])     # 앞부분 차수 확인
        for i in range(1, len(__n[1:])):     # 나머지 수열을 확인하며
            if int(__n[i]) + chasu != int(__n[i+1]) : # 차수 계산시 등차수열이 아니면
                Hansu = False
                break                           # 현재 수열 넘기기
        # 한수가 맞은경우
        if Hansu : 
            # print(f'한수: {cnt}, 차수: {chasu}, 개수: {result + 1}')
            result += 1
        cnt += 1
    print(result)