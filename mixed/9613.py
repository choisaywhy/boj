import sys
from itertools import combinations

N = int(sys.stdin.readline())

for _ in range(N):

    array = list(map(int, sys.stdin.readline().split()))
    array = array[1:]
    combi = combinations(array,2)
    answer = 0
    
    for A,B in combi:
        while B >0:
            A, B = B, A % B
        answer += A
    print(answer)