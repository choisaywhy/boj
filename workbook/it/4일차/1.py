import sys

def solution(n):
    if n == 1:
        print(1)
        return
    
    rooms = [1]
    cnt = 1

    while True:
        rooms.append(cnt*6 + rooms[cnt-1])
        if rooms[cnt-1] < n <= rooms[cnt]:
            print(cnt+1)
            break
        cnt += 1



if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    solution(n)