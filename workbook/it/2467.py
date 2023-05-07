import sys

def solution(N, sol):
    ans = 1e10
    sol.sort()
    left, right = 0, N-1
    curr_left, curr_right = 0, N-1
    while curr_left < curr_right:
        curr_val = sol[curr_left] + sol[curr_right]
        if abs(curr_val) < ans:
            ans = abs(curr_val)
            left = curr_left
            right = curr_right
        
        if curr_val <= 0:
            curr_left += 1
        else :
            curr_right -= 1
    
    print(sol[left], sol[right])



if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    sol = list(map(int, input().split()))
    solution(N, sol)


# dfs 재귀로 모든 조합 판별 -> time out
# import sys

# def solution(N, sol):
#     num = 1e9
#     ans = []
#     sol.sort()

#     def dfs(temp, idx):
#         nonlocal ans, num
#         print(temp,'turn')
#         if len(temp) == 2:
#             print('reached len 2')
#             if abs(sum(temp)) < num:
#                 print('sum is on the way')
#                 ans = temp
#                 num = abs(sum(temp))
#                 print('ans',ans,'num',num,'updated')
#             return
        
#         for i in range(idx,N):
#             dfs(temp+[sol[i]], i+1)

        

#     dfs([],0)
#     print(ans)



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     N = int(input())
#     sol = list(map(int, input().split()))
#     solution(N, sol)