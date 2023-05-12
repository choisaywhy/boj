import sys
from collections import deque


def solution(N, cars):

    answer = [-1] * N
    curr_time = -1
    waiting = [0, 0, 0, 0]
    while cars[0] or cars[1] or cars[2] or cars[3]:
        min_time = int(1e9)
        for i in range(4):
            if cars[i]:
                time = cars[i][0][1]
                min_time = min(min_time, time)
                if time <= curr_time:
                    waiting[i] = 1
        num = sum(waiting)

        if num == 4:
            break

        if num == 0:
            curr_time = min_time
            continue
        for i in range(4):
            if waiting[i] and not waiting[(i - 1) % 4]:
                idx, t = cars[i].popleft()
                answer[idx] = curr_time
        for i in range(4):
            waiting[i] = 0
        curr_time += 1
    print(*answer, sep='\n')


if __name__ == '__main__':
    input = sys.stdin.readline


    N = int(input())
    cars = [deque([]), deque([]), deque([]), deque([])]
    car_idx = {"A":0, "B":1,"C":2, "D":3}
    for i in range(N):
        t, w = map(str, input().split())
        cars[car_idx[w]].append((i, int(t)))

    solution(N, cars)