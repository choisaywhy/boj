# 나와 동일한 원소, 나와 값이 동일한 원소 중복처리 한꺼번에 하는 other's algo
import sys

def solution(N,M,arr) :

    def DFS(res):
        if len(res) == M : # 백트래킹, 길이를 만족하면 result 추가 후 return
            print(" ".join(map(str,res)))
            return

        revalue = 0
        for i in range(N) : 
            if visited[i] or revalue == arr[i] : # 같은 index 무시, 같은 값 무시
                continue
            visited[i] = True
            revalue = arr[i] # 동일 값 처리를 위해 현재 값 저장
            DFS(res + [arr[i]]) # res 업데이트 하여 재귀
            visited[i] = False

    visited = [False] * N
    DFS([])


if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    arr = sorted(list(map(int, input().split()))) # 사전 순으로 arr 할당

    solution(N,M,arr)

# import sys

# def solution(N,M,arr) :

#     def DFS(res,depth):
#         if depth == M : # 백트래킹, 길이를 만족하면 result 추가 후 return
#             print(" ".join(map(str,res)))
#             return

#         revalue = 0
#         for i in range(N) : 
#             if visited[i] or revalue == arr[i] : # 같은 index 무시, 같은 값 무시
#                 continue
#             visited[i] = True
#             revalue = arr[i]
#             DFS(res + [arr[i]], depth+1) # res 업데이트 하여 재귀
#             visited[i] = False

#     visited = [False] * N
#     DFS([],0)


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M = map(int, input().split())
#     arr = sorted(list(map(int, input().split()))) # 사전 순으로 arr 할당

#     solution(N,M,arr)



# 통과 but 최대 효율을 내지는 않음
# import sys

# def solution(N,M,arr) :
#     def DFS(res):
#         if len(res) == M : # 백트래킹, 길이를 만족하면 result 추가 후 return
#             result.append(res)
#             return
#         overlap = ""
#         for i in range(N) : 
#             if str(i) in res : # 같은 index 무시 (중복 제거)
#                 continue
#             DFS(res + str(i)) # res 업데이트 하여 재귀

#     result = []
#     new = []
#     DFS("")

#     # 'indexindexindex' -> (arr[index], arr[index] .. )
#     for re in result :
#         tmp = tuple(arr[int(r)] for r in re)
#         new.append(tmp)

#     # 중복 제거하여 사전순 출력
#     for re in sorted(list(set(new))) :
#         for r in re :
#             print(r, end=" ")
#         print()
# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split())) # 사전 순으로 arr 할당

#     solution(N,M,arr)


# 통과된 코드 i in res 대신 visited 추가
# import sys

# def solution(N,M,arr) :

#     def DFS(res):
#         if len(res) == M : # 백트래킹, 길이를 만족하면 result 추가 후 return
#             result.append(res)
#             return
        
#         for i in range(N) : 
#             if visited[i] :
#                 continue
#             visited[i] = True
#             DFS(res + str(i)) # res 업데이트 하여 재귀
#             visited[i] = False

#     result = []
#     new = []
#     visited = [False for _ in range(N)]

#     DFS("")

#     for re in result : # re = 'indexindexindex' -> (arr[index], arr[index] .. )
#         tmp = tuple(arr[int(r)] for r in re)
#         new.append(tmp)

#     # 중복 제거하여 사전순 출력
#     for re in sorted(list(set(new))) :
#         for r in re :
#             print(r, end=" ")
#         print()


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split())) # 사전 순으로 arr 할당
#     solution(N,M,arr)



# third trial
# 반례 
# 3 1
# 1 19 2
# 정렬 진행 시, 기준을 str으로 하여 잘못된 결과가 나옴
# import sys

# def solution(N,M,arr) :
#     def DFS(res):
#         if len(res) == M : # 백트래킹, 길이를 만족하면 result 추가 후 return
#             result.append(res)
#             return
        
#         for i in range(N) : 
#             if str(i) in res : # 같은 index 무시 (중복 제거)
#                 continue
#             DFS(res + str(i)) # res 업데이트 하여 재귀

#     result = []
#     new = []
#     DFS("")

#     for re in result :
#         tmp = " ".join(str(arr[int(r)]) for r in re)
#         new.append(tmp)

#     # 중복 제거하여 사전순 출력
#     for re in sorted(list(set(new))) :
#         print(re)


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M = map(int, input().split())
#     arr = sorted(list(map(int, input().split()))) # 사전 순으로 arr 할당
#     solution(N,M,arr)


# second trial 
# 시간초과, sort나 문자열로 바꾸는 부분을 dfs 쪽에서 사전 처리 하는 법을 고안해야 할듯 함
# import sys

# def solution(N,M,arr) :
#     def DFS(index, res):
#         if len(res) == M : # 백트래킹, 길이를 만족하면 result 추가 후 return
#             result.append(res)
#             return
        
#         for i in range(N) : 
#             if index == i : # 같은 index 무시 (중복 제거) --> M이 2 이상이 되는 경우에 틀림
#                 continue
#             DFS(i ,res + [arr[i]]) # res 업데이트 하여 재귀

#     result = []
#     DFS(N+1, [])
#     res = []
#     while result :
#         tmp = ' '.join(result.pop())
#         res.append(tmp)

#     # 중복 제거하여 사전순 출력
#     for re in sorted(list(set(res))) :
#         print(re)


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M = map(int, input().split())
#     arr = sorted(list(map(str, input().split()))) # 사전 순으로 arr 할당
#     solution(N,M,arr)


# first trial
# arr 내부 숫자 10,000 까지 limit이므로, 문자열 처리 부적절함
# import sys

# def solution(N,M,arr) :
#     def DFS(index, res):
#         if len(res) == M : # 백트래킹, 길이를 만족하면 result 추가 후 return
#             result.append(res)
#             return
        
#         for i in range(N) : 
#             if index == i : # 같은 index 무시 (중복 제거)
#                 continue
#             DFS(i ,res + arr[i]) # res 업데이트 하여 재귀

#     result = []
#     DFS(N+1, "")

#     # 중복 제거하여 사전순 출력
#     for re in sorted(list(set(result))) :
#         for r in re :
#             print(r, end=" ")
#         print()


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N, M = map(int, input().split())
#     arr = sorted(list(map(str, input().split()))) # 사전 순으로 arr 할당
#     solution(N,M,arr)