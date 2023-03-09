import sys

def solution(N,A,ops):
    max_val = -1000000001
    min_val = 1000000001

    def DFS(depth, total):
        nonlocal max_val, min_val

        if depth == N:
            max_val = max(max_val, total)
            min_val = min(min_val, total)
            return
        
        for i in range(4):
            if ops[i] == 0:
                continue

            ops[i] -= 1
            if i == 0:
                DFS(depth+1, total+A[depth])
            elif i == 1:
                DFS(depth+1, total-A[depth])
            elif i == 2:
                DFS(depth+1, total*A[depth])
            elif i == 3:
                if total < 0 :
                    DFS(depth+1, (-total)//A[depth]*-1)
                else:
                    DFS(depth+1, total//A[depth])
            ops[i] += 1
            
    DFS(1,A[0])
    print(max_val)
    print(min_val)



if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    A = list(map(int, input().split()))
    ops = list(map(int, input().split()))
    
    solution(N,A,ops)




# 1st trial
# import sys

# def solution(N,A,ops):
#     max_val = -1000000001
#     min_val = 1000000001
#     visited = [False]*(len(ops))

#     def DFS(depth, total):
#         nonlocal max_val, min_val

#         if depth == N:
#             max_val = max(max_val, total)
#             min_val = min(min_val, total)
#             return
        
#         for i in range(len(ops)):
#             if visited[i]:
#                 continue
#             visited[i] = True
#             if ops[i] == 0:
#                 DFS(depth+1, total+A[depth])
#             elif ops[i] == 1:
#                 DFS(depth+1, total-A[depth])
#             elif ops[i] == 2:
#                 DFS(depth+1, total*A[depth])
#             elif ops[i] == 3:
#                 if total < 0 :
#                     DFS(depth+1, (-total)//A[depth]*-1)
#                 else:
#                     DFS(depth+1, total//A[depth])
#             visited[i] = False
            
#     DFS(1,A[0])
#     print(max_val)
#     print(min_val)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N = int(input())
#     A = list(map(int, input().split()))
#     temp = list(map(int, input().split()))
#     ops = []
#     for i in range(4):
#         for _ in range(temp[i]):
#             ops.append(i)
    
#     solution(N,A,ops)