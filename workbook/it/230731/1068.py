import sys

def solution():
    n = int(input())
    parents = list(map(int,input().split()))
    leafs = {i:[] for i in range(n)}

    for c, p in enumerate(parents):
        if p == -1:
            continue
        leafs[p].append(c)
    
    count = 0 # 초기 리프노드 개수
    for i in range(n):
        if leafs[i] == []:
            count += 1

    r = int(input())
    if parents[r] == -1:
        print(0)
        return
    if len(leafs[parents[r]]) == 1: # 부모노드가 리프노드가 됨
        leafs[parents[r]] = []
        count += 1
    
    stack = [r]
    while stack:
        node = stack.pop()
        if leafs[node] == []:
            count -= 1
            continue
        
        stack.extend(leafs[node])
        leafs[node] = []


    print(count)



if __name__ == "__main__" :
    input = sys.stdin.readline
    
    solution()
