# 중복순열. 순서 상관안하는 순열. 1,1 가능. 2,1 1,2 가능
from itertools import product
n, m = map(int, input().split())
for i in product(map(str,list(range(1, n+1))), repeat=m): print(' '.join(i))
