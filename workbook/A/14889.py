import sys

def solution(N,S):
    ans = 1e19
    visited = [False]*N
    
    def DFS(depth,idx):
        nonlocal ans, visited
        if depth == N//2:
            start = 0
            link = 0
            for x in range(N):
                for y in range(x+1,N):
                    if not visited[x] and not visited[y]: # 다른 팀
                        link += S[x][y] + S[y][x]
                    elif visited[x] and visited[y]: # 현재 팀
                        start += S[x][y] + S[y][x]

            ans = min(ans, abs(start-link))
            return
        
        for x in range(idx, N):
            if visited[x]:
                continue
            visited[x] = True
            DFS(depth+1, x+1)
            visited[x] = False
    
    DFS(0,0)
    print(ans)



if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    solution(N,S)


# 시간 초과
# import sys

# def solution(N,S):
#     ans = 1e19
#     visited = [False]*N
#     def DFS(depth,visited):
#         nonlocal ans
#         if depth == N//2:
#             count = 0
#             oppsite_count = 0
#             for x in range(N):
#                 for y in range(x+1,N):
#                     if not visited[x] and not visited[y]: # 다른 팀
#                         oppsite_count += S[x][y] + S[y][x]
#                     elif visited[x] and visited[y]: # 현재 팀
#                         count += S[x][y] + S[y][x]

#             ans = min(ans, abs(count-oppsite_count))
#             return
        
#         for x in range(depth, N):
#             if visited[x]:
#                 continue
#             visited[x] = True
#             DFS(depth+1, visited)
#             visited[x] = False
    
#     DFS(0,visited)
#     print(ans)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N = int(input())
#     S = [list(map(int, input().split())) for _ in range(N)]

#     solution(N,S)









# 2nd trial
# import sys

# def solution(N,S,total):
#     ans = total
#     visited = [False]*N
#     def DFS(depth, count,visited):
#         nonlocal ans
#         if depth == N//2:
#             print(depth)
#             opposite = 0
#             for x in range(N):
#                 for y in range(N):
#                     if x == y or visited[x] or visited[y]:
#                         continue
#                     print(visited[x], visited[y])
#                     opposite += S[x][y]

#             ans = min(ans, abs(count-opposite)) # 상대 팀 능력치를 정확히 파악할 수 없음
#             print(visited, ans, opposite, count)

#             return
        
#         for x in range(N):
#             for y in range(x+1,N):
#                 if visited[x] or visited[y]:
#                     continue

#                 visited[x], visited[y] = True, True
#                 DFS(depth+1, count+S[x][y]+S[y][x],visited)
#                 visited[x], visited[y] = False, False
    
#     DFS(1, 0,visited)
#     print(ans,total)





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N = int(input())
#     total = 0
#     S = []
#     for _ in range(N):
#         S.append(list(map(int, input().split())))
#         total += sum(S[_])
#     solution(N,S,total)





# import sys

# def solution(N,S,total):
#     ans = total
#     def DFS(depth, count):
#         nonlocal ans
#         if depth == N/2:
#             ans = min(ans, abs(count-(total-count))) # 상대 팀 능력치를 정확히 파악할 수 없음
#             print(S, ans)

#             return
        
#         for x in range(N):
#             for y in range(N):
#                 if x == y:
#                     continue
#                 if S[x][y] != -1:
#                     temp1, temp2 = S[x][y], S[y][x]
#                     S[x][y], S[y][x] = -1, -1
#                     DFS(depth+1, count+temp1+temp2)
#                     S[x][y], S[y][x] = temp1, temp2
    
#     DFS(1, 0)
#     print(ans,total)





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N = int(input())
#     total = 0
#     S = []
#     for _ in range(N):
#         S.append(list(map(int, input().split())))
#         total += sum(S[_])
#     solution(N,S,total)