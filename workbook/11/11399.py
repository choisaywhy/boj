import sys

def solution(N, time):
    time.sort()
    res = 0
    total = 0
    for i in range(N) :
        res += time[i] + total
        total += time[i]
    
    print(res)



if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    time = list(map(int, input().split()))
    solution(N, time)