import sys
def solution(N, S, arr) :
    def DFS(depth, res): # 하나의 arr 원소에 대해 적용된다 할 때, 
        nonlocal count
        if depth == N :
            return
        if res + arr[depth] == S : # 해당 원소 포함 시
            count += 1
        
        DFS(depth+1, res) # 해당 원소 O
        DFS(depth+1, res+arr[depth]) # 해당 원소 X
    
    count = 0
    DFS(0,0)
    print(count)


if __name__ == "__main__" :
    input = sys.stdin.readline
    N, S = map(int, input().split())
    arr = list(map(int, input().split()))
    solution(N, S, arr)


# 2nd trial, res를 []화, s==0인 경우 res가 []임을 방지하기 위해
# import sys
# def solution(N, S, arr) :
#     def DFS(depth, res):
#         nonlocal count
#         if depth == N :
#             print('finished',res)
#             return
        
#         if sum(res)+arr[depth] == S : # 현재껄 더해줌
#             print(res,'answer')
#             count += 1

#         DFS(depth+1, res)
#         DFS(depth+1, res+[arr[depth]])
    
#     count = 0
#     DFS(0,[])
#     print(count)


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, S = map(int, input().split())
#     arr = list(map(int, input().split()))
#     solution(N, S, arr)


# first trial --> success, 알고리즘 적으로 풀이하지 못함
# import sys
# from itertools import combinations as cb
# def solution(N, S, arr) :
#     res = 0

#     for i in range(1,N+1) :
#         for combi in cb(arr, i) :
#             if sum(combi) == S :
#                 res += 1

#     print(res)


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, S = map(int, input().split())
#     arr = list(map(int, input().split()))
#     solution(N, S, arr)