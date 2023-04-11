import sys
from collections import deque, defaultdict

def solution(n, tree, root):

    idxs = defaultdict(list) # {level : [node 열 번호]}
    left, right = deque([]), deque([(root,1)])

    def DFS(node, level):
        l, r = tree[node]

        if l != -1:

            if not right or right[0] != (node, level):
                while left and left[-1] != (node, level): # node를 right[0]로 옮기기
                    right.appendleft(left.pop())
                right.appendleft(left.pop())
            
            left.append((l, level+1))
            DFS(l, level+1)

        if r != -1:
            if not left or left[-1] != (node, level):
                while right and right[0] != (node, level): # node를 left[-1]로 옮기기
                    left.append(right.popleft())
                left.append(right.popleft())
            right.appendleft((r, level+1))
            DFS(r, level+1)
    
    DFS(root,1)

    for i, v in enumerate(left+right):
        node, level = v
        idxs[level].append(i) # 각 level의 노드 열 번호 저장

    # 가장 긴 너비 연산
    max_length = 0
    max_level = 0
    for i in range(1,len(idxs)+1):
        length = max(idxs[i])-min(idxs[i])+1 
        if max_length < length:
            max_level = i
            max_length = length
    
    print(max_level, max_length)
        


if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    tree = [0]*(n+1)
    root = 0
    parents = [False]*(n+1)
    for _ in range(n):
        node, l, r = map(int, input().split())
        tree[node] = [l,r] # tree[parent_node] = [left_child, right_child]
        if r != -1: 
            parents[r] = True
        if l != -1:
            parents[l] = True
    for i in range(1,n+1):
        if not parents[i]:
            root = i # 트리의 root
    solution(n, tree, root)


# 문제 이해.. 오류!! 노드 번호가 아닌 열 번호를 비교해야함
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