# 중복조합, 연속수까진 포함되는 조합. 1,1 가능, 1,2 2,1 불가능
from itertools import combinations_with_replacement
n, m = map(int, input().split())
for i in combinations_with_replacement(map(str,list(range(1, n+1))), m): print(' '.join(i))
