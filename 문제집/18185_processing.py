import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
cost = 0
for index in range(N) :
    if not A[index] :
        continue

    if index == N - 2 or (index < N - 1 and A[index+1]):
        if index < N - 2 and A[index+1] <= A[index+2]:
            
            while A[index] :
                A[index] -= 1
                A[index+1] -= 1
                A[index+2] -= 1
                cost += 7
        else :
            
            while A[index] :
                A[index] -= 1
                A[index + 1] -= 1
                cost += 5
        
    if index == N - 1 or (index < N - 1 and not A[index+1]):
        while A[index] :
            A[index] -= 1
            cost += 3
    
print(cost)
    
    
    
        

