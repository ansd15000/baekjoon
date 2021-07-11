# n = int(input())
# a = [ list(map(int, input().split())) for _ in range(n)]
# b = sorted(a, key= lambda x: x[0], reverse= True)
# rank = 1
# ranks = []
# for i in range(n-1):
#     if b[i][1] > b[i + 1][1]: # 순서대로 정렬한 뒤, 키까지 크면
#         ranks.append(rank)
#         rank = i + 2
#     else: # 키가 이하면
#         ranks.append(rank)
# ranks.append(rank)
# # print(rank)
# print(' '.join(map(str,ranks)))

# for i, v in enumerate(b):
#     loc = a.index(v)
#     a[loc] = ranks[i]
# print(b)
# print(' '.join(map(str,a)))

# ===================================
# 키만 조따크면 정렬후 어케 처리할지. 알아보자
n = int(input())
a = [ list(map(int, input().split())) for _ in range(n)]

# 정렬 되있어야함
def makeRank(l):
    rank = 1
    ranks = []
    for i in range(n-1):
        t1 = l[i][0] > l[i+1][0] # 뒤보다 체중크면
        t2 = l[i][1] > l[i+1][1] # 뒤보다 키 크면
        if t1 and t2:
            ranks.append(rank)
            rank = i+2 # 순위변동 있을 떄, 비교대상의 랭크를 저장해둠.
        elif (t1 or t2) or (l[i][0] == l[i+1][0] and l[i][1] == l[i+1][1]): # 둘 중 하나만 크거나, 같으면
            ranks.append(rank)  # 랭크 저장
        else  :
            ranks.append(i+1)
    ranks.append(rank)
    return ranks


b = sorted(a, key=lambda x: x[0], reverse=True)
# print(b)
for i in range(n -1):
    for j in range(i+1, n):
        if b[i][1] < b[j][1]:
            b[i], b[j] = b[j], b[i]
# print(b)

# 순서 정렬
ranks = makeRank(b)
for i,v in enumerate(b):
    a[a.index(v)] = ranks[i]
print(' '.join(map(str,a)))

#============================================

# 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 # 나는 병신새끼입니다 
# n = int(input())
# a = [ list(map(int, input().split())) for _ in range(n) ]

# for i in a:
#     rank = 1
#     for j in a:
#         if i[0] < j[0] and i[1] < j[1]:
#             rank += 1
#     print(rank, end = ' ')

'''
8
22 110
22 110
55 185
88 186
60 175
46 155
33 111
58 183
'''

'''
7
99 110  # 아니 이놈은 어디에 있던간... 110 보다 안작으면 다른애들이랑은 다 덩치가 같은 축인데 이런건 왜 고려 안하냐 진짜 내가푼게 맞다고 생각한다고ㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗㅗ
88 186
60 175
58 183
55 185
46 155
33 111
'''

'''
5
55 185
58 183
55 185
55 185
55 185
'''

'''
10
1 1
1 2
1 3
2 2
2 2
2 3
4 1
4 4 <
4 0
5 5 <
'''