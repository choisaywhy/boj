import sys

def solution(N,M,r,c,d,room):
    directions = {0:(-1,0), 1:(0,1), 2:(1,0), 3:(0,-1)}
    cleaner = (r,c,d)
    ans = 0

    def check_clean(x,y) :
        if room[x][y] == 0 :
            return True
        return False

    while True :
        r,c,d = cleaner
        dr, dc = directions[d]
        flag = False
        print(r,c,d,'turn')
        
        # 1. 해당 칸 청소
        if room[r][c] == 0 :
            print('not cleaned yet')
            room[r][c] = -1
            ans += 1
            print(ans,'ans updated')
        
        # 2,3. 주변 탐색
        for _ in range(4) :
            nd = (d+3) % 4
            if check_clean(r+nr, c+nc):
                print('near by not cleaned yet',r+nr, c+nc, k)
                cleaner = (r + nr,  c + nc, k)
                print('cleaner updated',cleaner)
                flag = True
                break
        if flag :
            continue

        # 3
        if room[r-dr][c-dc] != 1 :
            print('can go back')
            cleaner = (r-dr, c-dc, d)
            print('cleaner updated',cleaner)
            continue
        else :
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