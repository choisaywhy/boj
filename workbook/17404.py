import sys

def solution(N, color):
    ans = 1e9
    
    for i in range(3): # 첫번째 집을 칠하는 색깔
        dp = [[1e9]*3 for _ in range(N)]
        dp[0][i] = color[0][i]

        for j in range(1,N):
            dp[j][0] = color[j][0] + min(dp[j-1][1], dp[j-1][2])
            dp[j][1] = color[j][1] + min(dp[j-1][0], dp[j-1][2])
            dp[j][2] = color[j][2] + min(dp[j-1][1], dp[j-1][0])
        

        for k in range(3):
            if i == k:
                continue
            ans = min(ans, dp[-1][k])
    
    print(ans)



if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    color = [list(map(int, input().split())) for _ in range(N)]

    solution(N, color)







# 1st strial
# import sys

# def solution(N, color):

#     first = [[0,1,2] for _ in range(N)]
#     print(color)

#     for i in range(1,N-1):

#         # r
#         if color[i-1][1] < color[i-1][2]:
#             color[i][0] += color[i-1][1]
#             first[i][0] = first[i-1][1]
#         else:
#             color[i][0] += color[i-1][2]
#             first[i][0] = first[i-1][2]
        
#         # g
#         if color[i-1][0] < color[i-1][2]:
#             color[i][1] += color[i-1][0]
#             first[i][1] = first[i-1][0]
#         else:
#             color[i][1] += color[i-1][2]
#             first[i][1] = first[i-1][2]

#         # b
#         if color[i-1][0] < color[i-1][1]:
#             color[i][2] += color[i-1][0]
#             first[i][2] = first[i-1][0]
#         else:
#             color[i][2] += color[i-1][1]
#             first[i][2] = first[i-1][1]
        

#     for i in range(3): # 맨 마지막 노드
#         print(i,'turn')
#         tmp = []
#         for j in range(3):
#             print('searcing',j)
#             print('first node',first[N-2][j], i)
#             if first[N-2][j] == i or i == j:
#                 continue
            
#             tmp.append(color[N-2][j])
#             print(color[N-2][j])
#             print('tmp updated',tmp)
        
#         if tmp:
#             color[N-1][i] += min(tmp)
#         if not tmp:
#             color[N-1][i] = 1e9

#     print(color)

#     print(min(color[-1]))





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N = int(input())
#     color = [list(map(int, input().split())) for _ in range(N)]

#     solution(N, color)