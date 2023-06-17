import sys

def solution(n,consult):
    
    dp = [0]*(n+2)

    for i in range(1,n+1):
        t,p = consult[i]
        dp[i] = max(dp[i-1], dp[i])
        if i+t < n+2:
            dp[i+t] = max(dp[i]+p, dp[i+t])

    print(max(dp[-1], dp[-2])) # for문이 마지막 date 처리 못하므로 둘 중 최댓값 반환해야함





if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    consult = [(0,0)]+[tuple(map(int, input().split())) for _ in range(n)]
    solution(n,consult)

# import sys

# def solution(n,consult):
    
#     dp = [0]*(n+2)

#     for i in range(1,n+1):
#         t,p = consult[i]
#         dp[i] = max(dp[i-1], dp[i])
#         if i+t < n+2:
#             dp[i+t] = max(dp[i]+p, dp[i+t])

#     print(max(dp))
        

# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     consult = [(0,0)]+[tuple(map(int, input().split())) for _ in range(n)]
#     solution(n,consult)