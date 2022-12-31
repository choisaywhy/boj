import sys

def solution(n, triangle):
    
    for x in range(1,n) :
        for y in range(x+1) :
            if y == 0 :
                triangle[x][y] += triangle[x-1][y]
            elif y == x :
                triangle[x][y] += triangle[x-1][y-1]
            else :
                triangle[x][y] += max(triangle[x-1][y-1], triangle[x-1][y])

    print(max(triangle[-1]))



if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    triangle = []
    for _ in range(n) :
        triangle.append(list(map(int, input().split())))
    
    solution(n, triangle)