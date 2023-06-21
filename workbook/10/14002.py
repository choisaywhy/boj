# 코드 개선
import sys

def solution(n,a):
    dp = [0]*(n+1)
    pre = [0]*(n+1)
    maxlen = 0

    for i in range(1,n+1):
        tmp = 0
        for j in range(i):
            if a[i] > a[j] and dp[j] > dp[tmp]:
                tmp = j
                pre[i] = j

        dp[i] = dp[tmp] + 1
        if dp[i] > dp[maxlen]:
            maxlen = i

    
    print(dp[maxlen])
    target = maxlen
    ans = []

    while target:
        ans.append(a[target])
        target = pre[target]
    
    print(" ".join(map(str, ans[::-1])))




if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    a = [0]+list(map(int, input().split()))
    solution(n,a)

    



# 1st trial success
# import sys

# def solution(n,a):
#     dp = [0]*(n+1)
#     pre = [0]*(n+1)
#     maxlen = 0

#     for i in range(1,n+1):
#         tmp = 0
#         for j in range(i-1,0,-1):
#             if a[i] > a[j] and dp[j] > dp[tmp]:
#                 tmp = j
#                 pre[i] = j

#         dp[i] = dp[tmp] + 1
#         if dp[i] > dp[maxlen]:
#             maxlen = i

    
#     print(dp[maxlen])
#     target = maxlen
#     ans = []

#     while target:
#         ans.append(a[target])
#         target = pre[target]
    
#     print(" ".join(map(str, ans[::-1])))




# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     a = [0]+list(map(int, input().split()))
#     solution(n,a)

    