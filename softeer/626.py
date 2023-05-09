# 회의실 예약
import sys

input = sys.stdin.readline
N, M = map(int, input().split())

rooms = {}

for _ in range(N):
    rooms[str(input().strip())] = [False] * 9 # false when its empty

for _ in range(M):
    r, s, t = map(str, input().strip().split())
    for time in range(int(s)-9,int(t)-9):
        rooms[r][time] = True



## print
walls = N-1
for room in sorted(rooms.keys()):
    print("Room ",room,":",sep="")
    
    ans = []
    temp = []
    for i in range(9):
        if not rooms[room][i]: # 비어있으면
            temp.append(i+9)
            if i == 8:
                ans.append(temp)
            continue
        if temp:
            ans.append(temp)
            temp = []
    
    if not ans:
        print("Not available")
    else:
        print(len(ans),"available:")
        for time in ans:
            s,t = time[0],time[-1]+1

            print(str(s).zfill(2),"-",str(t).zfill(2), sep="")

    if walls > 0:
        print("-----")
        walls -= 1