import sys

def solution(T):
    for _ in range(T) :
        ox = str(input().strip())
        count = 0
        temp = 0
        for s in ox :
            if s == "O" :
                count += 1
                temp += 1
                if temp > 1 :
                    count += temp - 1
            else :
                temp = 0
        print(count)





if __name__ == "__main__" :
    input = sys.stdin.readline
    T = int(input())

    solution(T)