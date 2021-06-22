import sys
# a = [int(sys.stdin.readline().rstrip()) for _ in range(10)]
# res = {i % 42 for i in a} # set comprehension. set으로 중복제거
# print(len(res))
    
a = [int(sys.stdin.readline().rstrip()) % 42 for _ in range(10)]
print(len(set(a))) # 걍 리스트를 set으로 변경해줄수도 있네