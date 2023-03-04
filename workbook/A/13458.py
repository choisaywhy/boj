import sys

def solution(N : int, A : list, B : int, C : int)->None:
    ans = 0

    for _ in range(N) :
        students = A[_]- B
        ans += 1

        if students < 0 :
            continue
        ans += students // C
        if students % C > 0 :
            ans += 1
    
    print(ans)



if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())
    solution(N, A, B, C)