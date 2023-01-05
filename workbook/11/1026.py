import sys

def solution(N, A, B):
    A.sort()
    B.sort(reverse = True)
    res = 0

    for i in range(N) :
        res += A[i] * B[i]
    
    print(res)





if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    solution(N, A, B)