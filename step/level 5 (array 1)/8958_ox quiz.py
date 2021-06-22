import sys

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    a = sys.stdin.readline()
    score = 0
    defaultScore = 0
    for i in a:
        if i == 'O': defaultScore += 1
        else : defaultScore = 0
        score += defaultScore
    print(score)

'''
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
'''