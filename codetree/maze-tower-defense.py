import sys
input = sys.stdin.readline



def maze_to_linear():
    linear = []

    x,y = n//2, n//2
    direct = 2
    depth, count  = 1,0 # 1,2,3 씩 삭제, 2번 반복
    tmp_monster = 0

    while tmp_monster < monster:
        x,y = x+dx[direct], y+dy[direct]
        count += 1
        linear.append(maze[x][y])
        tmp_monster += 1

        if count == depth:
            direct = (direct+1)%4
        elif count // depth == 2:
            count = 0
            depth += 1
            direct = (direct+1)%4
    
    return linear

def linear_to_maze(linear):
    global maze
    new_maze = [[0]*n for _ in range(n)]

    x,y = n//2, n//2
    direct = 2
    depth, count  = 1,0 # 1,2,3 씩 삭제, 2번 반복

    for l in linear:
        if l == 0:
            continue
        x,y = x+dx[direct], y+dy[direct]
        count += 1
        new_maze[x][y] = l

        if count == depth:
            direct = (direct+1)%4
        elif count // depth == 2:
            count = 0
            depth += 1
            direct = (direct+1)%4
    
    maze = new_maze



def remove_repeated():
    global ans
    linear = maze_to_linear()
    tmp = []

    count = 1
    for i in range(1,len(linear)):
        if linear[i] == linear[i-1]:
            count += 1
        else:
            count = 1
            if count >= 4:
                ans += count*linear[i-1]
                tmp = tmp[:-count]
                continue
        tmp.append(linear[i])
    if len(tmp)==len(linear):
        return False
    
    fill_blank()

    return True


def attack(d,p):
    global monster
    global ans
    x,y = n//2, n//2

    for _ in range(p):
        x,y = x+dx[d], y+dy[d]
        ans += maze[x][y]
        maze[x][y] = 0
        monster -= 1
    
    fill_blank()


def fill_blank():
    global maze
    linear = maze_to_linear()
    tmp = []

    for l in linear:
        if l == 0:
            continue
        tmp.append(l)
    
    linear_to_maze(tmp)



    
def refill_maze():
    linear = maze_to_linear()
    tmp = []

    count = 1
    for i in range(1,len(linear)):
        if linear[i] == linear[i-1]:
            count += 1
        else:
            count = 1
            tmp.extend([count, linear[i]])

    linear_to_maze(tmp)
    



n,m = map(int,input().split())
ans = 0
maze = [list(map(int,input().split())) for _ in range(n)]
monster = n*n
for i in range(n):
    monster -= maze[i].count(0)
dx = [0,1,0,-1]
dy = [1,0,-1,0]
for _ in range(m):
    d,p = map(int,input().split())
    attack(d,p)
    
    while True:
        if not remove_repeated():
            break
    refill_maze()
        
