import sys

def solution(n,building):
    dp = [0]*n
    for i in range(n):
        stack = []
        for j in range(i+1, n):

            if not stack or ((building[j]-building[i])/(j-i))*(stack[-1]-i)+building[i] > building[stack[-1]]:
                stack.append(j)
                dp[j] += 1

        dp[i] += len(stack)
    print(max(dp))




if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    building = list(map(int,input().split()))
    solution(n,building)




# 문제 해독 wrong
# import sys

# def solution(n,building):
#     dp = [0]*n
#     for i in range(n):
#         stack = []
#         for j in range(i+1, n):

#             if not stack or stack[-1] < building[j]:
#                 stack.append(building[j])
#                 dp[j] += 1

#             if building[i] <= stack[-1]:
#                 break
#         dp[i] += len(stack)

#     print(max(dp))




# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     building = list(map(int,input().split()))
#     solution(n,building)
