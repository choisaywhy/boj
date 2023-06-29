import sys

def solution(n,a,k):
    a[a.index(-1)] = k
    a.sort()

    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None
    
    def bst(nodes):
        if not nodes:
            return None
        
        mid = len(nodes) // 2
        root = Node(nodes[mid])

        root.left = bst(nodes[:mid])
        root.right = bst(nodes[mid+1:])

        return root
    
    def postorder(root):
        if root:
            postorder(root.left)
            postorder(root.right)
            print(root.data, end=" ")
    
    tree = bst(a)
    postorder(tree)




if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    a = list(map(int,input().split()))
    k = int(input())
    solution(n,a,k)

    