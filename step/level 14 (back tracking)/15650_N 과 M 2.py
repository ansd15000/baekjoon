# 조합 (중복을 허용하지 않는 수열, 순서를 고려하지 않기때문에 1,2이 있다면 2,1 은 안됨)
from itertools import combinations
n , m = map(int, input().split())
for i in combinations(map(str, range(1, n +1)), m) : print(' '.join(i))