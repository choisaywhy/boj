import sys

def solution(N,M,nheard,nseen):
    
    res = set(nheard) & set(nseen)
    print(len(res))
    print("\n".join(sorted(list(res))))





if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    nheard = [str(input().strip()) for _ in range(N)]
    nseen = [str(input().strip()) for _ in range(M)]
    solution(N,M,nheard,nseen)