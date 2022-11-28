import sys

def solution(N, M):

    def DFS(res) :

        if len(res) == M :
            print(" ".join(res))
            return

        for i in range(1,N+1) :
            if str(i) in res :
                continue
            DFS(res+[str(i)])  
    DFS([])


if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    solution(N, M)



# 1st trial
# import sys
# from collections import deque

# input = sys.stdin.readline

# def DFS(N, start) :
#     stack = deque([start])
#     visited = [False for _ in range(N)]

#     while stack :
#         node = stack.pop()
#         if not visited[node] :
#             print(node, sep=" ")
#             visited[node] = True
#             for i in range(N) :
#                 if visited[i] :
#                     continue
#                 stack.append(i)
#     return stack               
    


# N, M = map(int, input().split())

# for i in range(N) :
#     DFS(N, i)
#     print()