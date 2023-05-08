import sys

def solution(turtle):
    directions = [(1,0),(0,1),(-1,0),(0,-1)] # 상우좌하
    maxx, minx, maxy, miny = 0,0,0,0
    x,y = 0,0
    target = 0
    for t in turtle:
        if t == "F":
            x += directions[target][0]
            y += directions[target][1]
        elif t == "B":
            x += directions[(target+2)%4][0]
            y += directions[(target+2)%4][1]
        elif t == "L":
            target = (target+3)%4
            continue
        elif t == "R":
            target = (target+1)%4
            continue
        
        if x < minx:
            minx = x
        elif x > maxx:
            maxx = x

        if y < miny:
            miny = y
        elif y > maxy:
            maxy = y
    
    print(abs((maxy-miny)*(maxx-minx)))




if __name__ == "__main__" :
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        turtle = list(map(str, input().strip()))
        solution(turtle)