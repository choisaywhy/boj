import sys

def solution(N,M,r,c,d,room):
    directions = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}
    cleaner = (r,c,d)
    ans = 0

    while True :
        r,c,d = cleaner
        dr, dc = directions[d]
        flag = False
        
        # 1. 해당 칸 청소
        if room[r][c] == 0 :
            room[r][c] = -1
            ans += 1
        
        # 2,3. 주변 탐색
        nd = d
        for _ in range(4) :
            nd = (nd+3) % 4
            nr, nc = directions[nd]
            if room[r+nr][c+nc] != 0:
                continue
            cleaner = (r + nr, c + nc, nd)
            flag = True
            break
        if flag :
            continue

        # 2
        if room[r-dr][c-dc] != 1 :
            cleaner = (r-dr, c-dc, d)
            continue
        break
    
    print(ans)




if __name__ == "__main__" :
    input = sys.stdin.readline
    N, M = map(int, input().split())
    r,c,d = map(int, input().split())
    room = []
    for _ in range(N):
        room.append(list(map(int, input().split())))
    solution(N,M,r,c,d,room)