# 2nd trial
# 무한루프 아니라 걍 개오래 걸리는거였음 ㄷㄷ 통과
import sys

def solution(n,eggs):
    ans = 0
    def dfs(idx, count):
        nonlocal ans
        # print(idx,count,eggs,'turn')

        if idx == n or count == n:
            if count > ans:
                ans = count
            return
        if eggs[idx][0] <= 0: # 현재 계란이 이미 깨진 경우
            dfs(idx+1, count)
        else:
            if count == n-1: # 나 빼고 다 깨진 경우
                dfs(n, count)
            else:
                for next in range(n):
                    if next == idx or eggs[next][0] <= 0 :
                        continue
                    eggs[idx][0] -= eggs[next][1]
                    eggs[next][0] -= eggs[idx][1]
                    tcount = count
                    if eggs[idx][0] <= 0:
                        tcount += 1
                    if eggs[next][0] <= 0:
                        tcount += 1

                    dfs(idx+1, tcount)
                    eggs[idx][0] += eggs[next][1]
                    eggs[next][0] += eggs[idx][1]
        
    dfs(0,0)
    print(ans)

if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    eggs = [list(map(int,input().split())) for _ in range(n)] # 내구도, 무게
    solution(n,eggs)

    
# 1st trial failed
# import sys

# def solution(n,eggs):
#     ans = []
#     def dfs(idx, broken, bcount):
#         nonlocal ans

#         # if idx == n-1 or bcount == n:
#         #     print(idx,n,'finishing line')
#         #     ans.append(bcount)
#         #     return
#         if idx == n or bcount == n or broken[idx]:
#             ans.append(bcount)
#             return
        
#         for next in range(n):
#             if next == idx or broken[next] :
#                 continue
#             s1, w1 = eggs[idx]
#             s2, w2 = eggs[next]
#             eggs[idx][0] -= w2
#             eggs[next][0] -= w1
#             tcount = bcount
#             if eggs[idx][0] <= 0:
#                 broken[idx] = True
#                 tcount += 1
#             if eggs[next][0] <= 0:
#                 broken[next] = True
#                 tcount += 1

#             dfs(idx+1, broken, tcount)
#             eggs[idx][0] = s1
#             eggs[next][0] = s2
#             broken[idx] = False
#             broken[next] = False
        
#     dfs(0, [False]*n,0)
#     print(max(ans))

# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     eggs = [list(map(int,input().split())) for _ in range(n)] # 내구도, 무게
#     solution(n,eggs)

    