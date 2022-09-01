import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline
N, K = map(int,input().split())

def solution(N,K):
    if N == K or K == 0:
        return 1
    return solution(N-1,K) + solution(N-1, K-1)

print(solution(N,K) % 1000000007 )