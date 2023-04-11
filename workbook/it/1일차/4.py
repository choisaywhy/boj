import sys
from collections import deque
def solution(n, tree):
    levels = [[] for _ in range(n+1)]
    print(tree)
    
    def DFS():
        stack = [(1,1)] # node, level
        visited = [False]*(n+1)

        while stack:
            node, level = stack.pop()
            

    def BFS(start):
        queue = deque([(start, 1)]) # node, level
        # visited = [False]*(n+1)
        # visited[1] = True

        while queue:
            node, level = queue.popleft()
            print(node, level,'turn')
            for next in tree[node]:
                print('next',next)
                # if next == -1 or visited[next]:
                if next == -1 :
                    continue
                levels[level+1].append(next)
                queue.append((next,level+1))
                print(level+1, levels[level+1],'updated')
    
    BFS(1)


if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    tree = [0]*(n+1)
    for _ in range(n):
        node, l, r = map(int, input().split())
        tree[node] = [l,r]

    solution(n, tree)



# import sys
# from collections import deque
# def solution(n, tree):
#     levels = [[] for _ in range(n+1)]
#     print(tree)

#     def BFS(start):
#         stack = deque([(start, 1)]) # node, level
#         # visited = [False]*(n+1)
#         # visited[1] = True

#         while stack:
#             node, level = stack.popleft()
#             print(node, level,'turn')
#             for next in tree[node]:
#                 print('next',next)
#                 # if next == -1 or visited[next]:
#                 if next == -1 :
#                     continue
#                 levels[level+1].append(next)
#                 stack.append((next,level+1))
#                 print(level+1, levels[level+1],'updated')
    
#     BFS(1)

#     print(levels)
#     max_length = 0
#     max_level = 0
#     for i in range(1,n+1):
#         if levels[i] == []:
#             break
        
#         levels[i].sort()
#         length = levels[i][-1] - levels[i][0] + 1

#         if  length > max_length:
#             max_level = i
#             max_length = length
    
#     print(max_level, max_length)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     tree = [0]*(n+1)
#     for _ in range(n):
#         node, l, r = map(int, input().split())
#         tree[node] = [l,r]

#     solution(n, tree)