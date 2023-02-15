import sys

def solution(N, arr):
    checked = [0] * (N+1)
    for i, v in enumerate(arr) :
        checked[v] = i
    ans = 1
    maxi = 0
    
    for i in range(1,N) :
        if checked[i] < checked[i+1] :
            ans += 1
        else :
            maxi = max(maxi, ans)
            ans = 1
    print(N - max(maxi, ans))
    


if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    arr = list(map(int, input().split()))
    solution(N, arr)


# 1차 시도 
# 반례 1 3 2 4 5 (정답 : 2, 출력 : 1)
# 더 긴 증가 부분 배열이 있음을 간과
# import sys

# def solution(N, arr):
#     checked = [False]*(N+1)
#     ans = 1

#     for a in arr :
#         print(a,'turn')
#         if a != N :
#             if not checked[a+1] :
#                 ans += 1
#                 print('ans updated',ans)
#         checked[a] = True
#         print(checked,a,'updated')
#     print(N-ans)





# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N = int(input())
#     arr = list(map(int, input().split()))
#     solution(N, arr)