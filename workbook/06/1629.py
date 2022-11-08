import sys

input = sys.stdin.readline


def multifly(A,B,C) :
    if B == 1 :
        return A % C
    
    res = multifly(A,B//2,C)
    if B % 2 == 0 :
        return (res * res) % C
    else :
        return (res * res * (A%C)) % C



A, B, C = map(int, input().split())
print(multifly(A,B,C))
