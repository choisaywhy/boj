import sys

def solution(N,schedule):
    schedule.sort(key = lambda a: a[0])
    schedule.sort(key = lambda a: a[1])

    count = 0
    pointer = 0

    for start, end in schedule :
        if start >= pointer :
            count += 1
            pointer = end
    print(count)




if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    schedule = []
    for _ in range(N) :
        schedule.append(tuple(map(int, input().split())))
    solution(N,schedule)