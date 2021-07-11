# 순열 구하기. (중복없고, 수가 연속되지 않고, 앞 뒤가 다르면 다른 값)
from itertools import permutations
n , m = map(int, input().split())
a = list(permutations(map(str, range(1,n+1)), m))
for i in a:
    print(' '.join(i))

# 라이브러리가 더 빠르지만 직접 구현하는 로직.. 이해하기 너무 어렵다 진짜
# n = 3; m = 3

# def permutations(arr, r):   # 시작할 첫번째 시작배열, m 길이의 순열
#     arr = sorted(arr)
#     used = [0] * len(arr)   # 사용한 숫자 누적 리스트

#     def generate(chosen, used): # 빈 리스트(결과값), 0 초기화 사용할 수 길이 리스트
#         if len(chosen) == r :   # chosen 길이가 순열길이와 같다면 종료.
#             print(chosen)
#             return 
        
#         for i in range(len(arr)):   # 순열 길이만큼 반복
#             if not used[i]:         # 만약 반복수 위치의 used의 값이 0이면
#                 chosen.append(arr[i])   # 입력된 수열 넣고
#                 used[i] = 1             # 현 반복위치 값을 True로 변경
#                 generate(chosen, used)  # 재기. [1,2,3,4], [1,0,0,0] -> print([1,2,3,4])
#                 used[i] = 0             # 해당위치 0으로 바꾸고 
#                 chosen.pop()            # chosen 맨 뒷자리 삭제 [1,2,3] ... 반복
#     generate([], used)

# permutations(list(range(1,n + 1)), m)