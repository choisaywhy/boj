import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
tree = {}

class Node:
    def __init__(self,item,left,right):
        self.item, self.left, self.right = item, left, right

for _ in range(N):
    item, left, right = list(map(str, input().strip().split()))
    if left == "." :
        left = None
    if right == "." :
        right = None
    tree[item] = Node(item,left,right)


def preorder(node) :
    print(node.item, end="")
    if node.left :
        preorder(tree[node.left])
    if node.right :
        preorder(tree[node.right])


def inorder(node) :
    if node.left :
        inorder(tree[node.left])
    print(node.item, end="")
    if node.right :
        inorder(tree[node.right])


def postorder(node) :
    if node.left :
        postorder(tree[node.left])
    if node.right :
        postorder(tree[node.right])
    print(node.item, end="")


preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])








# import sys
# from collections import deque

# input = sys.stdin.readline

# N = int(input())
# graph = {}

# for _ in range(N):
#     nodes = list(map(str, input().strip().split()))
#     graph[nodes[0]] = nodes[1:]

# def preorder(graph,root):
#     stack = deque([root])
#     visited = deque()

#     while stack :
#         node = stack.pop()
#         if node == ".":
#             continue
#         if node not in visited :
#             visited.append(node)
#             stack.extend(graph[node][::-1])
#     return "".join(visited)


# def inorder(graph,root):
#     stack = deque([root])
#     visited = []
#     answer = []

#     while stack :
#         node = stack.pop()
#         if node == ".":
#             if not visited:
#                 break
#             answer.append(visited.pop())
#             continue
#         if node not in visited:
#             visited.append(node)
#             stack.extend(graph[node][::-1])
                
#     return "".join(answer)





# print(preorder(graph,"A"))
# print(inorder(graph,"A"))
# print(postorder(graph,"A"))

