# 길이 짧은것부터, 같으면 사전순

from sys import stdin
a = list(set(stdin.readline().rstrip() for _ in range(int(stdin.readline()))))
# a.sort(key = lambda x : len(x))
# l = []
# flag = 0
# for i in range(len(a)-1):
#     if len(a[i]) != len(a[i+1]): 
#         l += sorted(a[flag:i+1]) # 길이 같은애들끼리만 정렬 후 리스트 확장.
#         flag = i + 1
# l += sorted(a[flag:]) # 마지막 요소는 포함되지 않으니 수동으로 추가. 이 땜에 for문이 후반에 의미없는 반복을 하는데.. 어떻게 해야 낭비가 없을까
# print('\n'.join(l))

a.sort() # 먼저 순서대로 정렬후
a.sort(key = lambda x: len(x)) # 길이정렬. 중복길이는 앞서 정렬한것땜에 알맞게 되겠지. ㅋㅋㅋㅋ
print('\n'.join(a))

'''
13
but
i
wont
zesita
no
more
no
more
it
cannot
wait
im
yours
'''