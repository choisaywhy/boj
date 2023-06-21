import sys

def solution(n,eggs):
    ans = []
    def dfs(idx, broken):
        if idx == n:
            print(idx,n,'finishing line')
            count = 0
            for b in broken:
                if b:
                    count += 1
            ans.append(count)
            return
        
        for next in range(n):
            if next == idx or broken[next] or broken[idx]:
                continue
            s1, w1 = eggs[idx]
            s2, w2 = eggs[next]
            eggs[idx][0] -= w2
            eggs[next][0] -= w1
            if eggs[idx][0] <= 0:
                broken[idx] = True
            if eggs[next][0] <= 0:
                broken[next] = True
            dfs(idx+1, broken)
            eggs[idx][0] = s1
            eggs[next][0] = s2
            broken[idx] = False
            broken[next] = False
        
    dfs(0, [False]*n)
    print(ans)

if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    eggs = [list(map(int,input().split())) for _ in range(n)] # 내구도, 무게
    solution(n,eggs)

    