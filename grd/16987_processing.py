# https://hangjastar.tistory.com/264 2nd trial 진행 중
import sys

def solution(n,eggs):
    ans = []
    def dfs(idx, bcount):
        nonlocal ans
        print(idx,bcount,'turn')

        # if idx == n-1 or bcount == n:
        #     print(idx,n,'finishing line')
        #     ans.append(bcount)
        #     return
        if idx == n or bcount == n or eggs[idx] <= 0:
            ans.append(bcount)
            return
        
        for next in range(n):
            if next == idx or eggs[next] <= 0 :
                dfs(idx+1, tcount)
                continue
            s1, w1 = eggs[idx]
            s2, w2 = eggs[next]
            eggs[idx][0] -= w2
            eggs[next][0] -= w1
            tcount = bcount
            if eggs[idx][0] <= 0:
                tcount += 1
            if eggs[next][0] <= 0:
                tcount += 1

            dfs(idx+1, tcount)
            eggs[idx][0] = s1
            eggs[next][0] = s2
        
    dfs(0,0)
    print(ans)
    print(max(ans))

if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    eggs = [list(map(int,input().split())) for _ in range(n)] # 내구도, 무게
    solution(n,eggs)

    

# 무한 루프
# import sys

# def solution(n,eggs):
#     ans = []
#     def dfs(idx, broken, bcount):
#         nonlocal ans
#         print(idx, broken,bcount,'turn')

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
#     print(ans)
#     print(max(ans))

# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     eggs = [list(map(int,input().split())) for _ in range(n)] # 내구도, 무게
#     solution(n,eggs)

    