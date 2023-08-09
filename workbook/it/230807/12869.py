import sys
from itertools import permutations as ptt

def solution():
    n = int(input())
    hp = list(map(int,input().split())) + [0]*(3-n)
    dp = [[[61]*61 for _ in range(61)] for _ in range(61)]

    ans = 1e6

    def dfs(x,y,z,attack):
        if x <= 0 and y <=0 and z <= 0: # 다 죽임
            ans = min(ans, attack)
            return
        
        # dp 비교위해 0으로 통일
        x = x if x > 0 else 0
        y = y if y > 0 else 0
        z = z if z > 0 else 0
        
        if dp[x][y][z] <= attack:
            return
        
        dp[x][y][z] = attack

        for nx,ny,nz in ptt([1,3,9],3):
            dfs(x-nx,y-ny,z-nz,attack+1)

    dfs(hp[0],hp[1],hp[2],0)
    print(ans)

if __name__ == "__main__" :
    input = sys.stdin.readline
    
    solution()
