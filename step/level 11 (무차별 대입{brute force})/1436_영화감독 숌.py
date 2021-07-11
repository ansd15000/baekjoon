# 5666 다음으론 6660 이 된다고 한다... 6666 보다 작기 때문에..
# 입력값이 최대 10000 이라 아슬아슬했지, 자릿수 늘어나면 답 없는 코드네
a = int(input())
i = 666
l = 0
while l != a:
    if str(i).count('666') >= 1: l += 1
    i +=1
print(i-1)

# 60밀리초 실행속도 코드... 머리아프니까 잘짜려고 노력하는건 나중을 기약하자.
# N = int(input())
# front = 0
# back = 0
# fronttemp = 0
# backlength = 0
# backlimit = 0
# pos = -1
# state = 'front'

# for _ in range(N-1) :
#     if state == 'front' :
#         front += 1
#         pos = str(front*100 + 66).find('666') # 왜 하필 66을 더하는지?
#         if pos != -1 :
#             state = 'back'
#             backlength = len(str(front)) - pos
#             backlimit = 10**backlength
#             fronttemp = front // backlimit
#             back = 0
#     else :
#         back += 1
#         if back >= backlimit :
#             state = 'front'
#             front += 1

# if state == 'front' :
#     print(front*1000 + 666)
# else :
#     print((fronttemp*1000 + 666)*backlimit + back)

# front       = 0   ,   1 ,   2,
# pos         = -1  ,  -1 ,  -1,
# state       = 'F' , 'B' , 'F',
# backlength  = 0   ,   0 ,   0,
# backlimit   = 0   ,   1 ,   1,
# fronttemp   = 0   ,   1 ,   2,
# back        = 0   ,   0 ,   1,
