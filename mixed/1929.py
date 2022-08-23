from re import L
import sys
from math import sqrt

def primary(M:int,N:int):
    array = [True] * (N + 1)
    array[0], array[1] = False, False

    for i in range(2, N+1):
        if array[i] :
            j = 2
            while i*j <= N:
                array[i*j] = False
                j += 1

    return array



M, N = map(int,sys.stdin.readline().split())

array = primary(M,N)

for i in range(M,len(array)):
    if array[i]:
        print(i)