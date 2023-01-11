import sys

def solution(N, level):
    last = level[-1]
    count = 0
    for l in range(N-2, -1, -1) :
        while level[l] >= last :
            level[l] -= 1
            count += 1
        
        last = level[l]

    print(count)




if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    level = []
    for _ in range(N) :
        level.append(int(input()))
    solution(N, level)