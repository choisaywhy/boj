# 중복값이 queue에 들어있을 때 처리 불가함
# https://www.acmicpc.net/source/61710104 참고
import sys
from heapq import *
def solution(k,operations):
    
    queue_max = []
    queue_min = []

    deleted = {}

    for op, val in operations:
        val = int(val)

        if op == "I":
            heappush(queue_max, -val)
            heappush(queue_min, val)
            if deleted.get(val, False):
                deleted[val] = False

        elif op == "D":
            if val == 1:
                if not queue_max:
                    continue
                tmp = -heappop(queue_max)
                while queue_max and deleted.get(tmp, False): # 이미 지워졌으면
                    deleted[tmp] = False
                    tmp = heappop(queue_max)
                deleted[tmp] = True
            elif val == -1:
                if not queue_min:
                    continue
                tmp = heappop(queue_min)
                while queue_min and  deleted.get(tmp, False): # 이미 지워졌으면
                    deleted[tmp] = False
                    tmp = heappop(queue_min)

                deleted[tmp] = True

    print(queue_min, queue_max)
    print(deleted)

    while queue_max and deleted.get(-queue_max[0], False):
        heappop(queue_max)
    while queue_min and deleted.get(queue_min[0], False):
        heappop(queue_min)
    
    if not queue_min or not queue_max:
        print("EMPTY")
    else:
        print(-heappop(queue_max), heappop(queue_min))


if __name__ == "__main__" :
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):

        k = int(input())
        operations = [tuple(map(str, input().strip().split())) for _ in range(k)]

        solution(k,operations)