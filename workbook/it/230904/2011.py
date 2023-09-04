import sys
def solution():
    mes = list(input().strip())
    nums = {1:(0,1,2,3,4,5,6,7,8,9), 2:(0,1,2,3,4,5,6)}
    n = len(mes)
    dp = [0]*(n+1)
    
    if int(mes[0]) == 0:
        return 0

    dp[0], dp[1] = 1,1

    for i in range(2,n+1):
        if int(mes[i-2]) in nums.keys() and int(mes[i-1]) in nums[int(mes[i-2])]: # 두자리로 새로운 경우의수 만드는 경ㅜ
            dp[i] += dp[i-2]
        else: # 안되는 경우 중
            if int(mes[i-1]) == 0: # 현재 값이 0인 경우
                return 0
        if int(mes[i-1]) != 0: # 현재 값이 단독으로 쓰일 수 있는 경우
            dp[i] += dp[i-1]
        dp[i] %= 1000000
    return dp[-1]



if __name__ == "__main__" :
    input = sys.stdin.readline

    print(solution())



# import sys
# def solution():
#     mes = list(input().strip())
#     n = len(mes)
#     dp = [0]*(n+1)
    
#     if mes[0] == 0:
#         return 0

#     dp[0], dp[1] = 1,1

#     for i in range(2,n+1):
#         if 0<int(mes[i-2]) < 3 and int(mes[i-1]) < 7:
#             dp[i] += dp[i-2]
#         else:
#             if mes[i-1] == 0:
#                 return 0
#         dp[i] += dp[i-1]
    
#     return dp[-1]% 1000000



# if __name__ == "__main__" :
#     input = sys.stdin.readline

#     print(solution())
