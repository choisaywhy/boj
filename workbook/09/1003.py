import sys

def solution(T):   

    for _ in range(T) :
        N = int(input())
        if N == 0 :
            print(1, 0)
            continue
        dp = [0 for _ in range(N+1)]
        dp[N] = 1
        for n in range(N,1,-1) :
            dp[n-1] += dp[n]
            dp[n-2] += dp[n] 
        
        print(dp[0], dp[1])



if __name__ == "__main__" :
    input = sys.stdin.readline
    T = int(input())

    solution(T)