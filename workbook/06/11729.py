import sys

input = sys.stdin.readline

def hanoi(N, A, B) :
    if N == 1:
        print(A, B)
        return
    hanoi(N-1, A, 6-A-B)
    print(A,B)
    hanoi(N-1, 6-A-B, B)





N = int(input())
print(2**N-1)
hanoi(N,1,3)