import sys
import heapq as hq

def solution(N, dots) :
    dots.sort()
    ans = [dots[0]]
    count = 0

    for x,y in dots[1:] :
        flag = False
        while ans :
            px, py = hq.heappop(ans)

            if px <= x <= py :
                if y > py :
                    hq.heappush(ans, (px, y))
                else :
                    hq.heappush(ans, (px, py))
                flag = True
                break
            else :
                count += py - px
        if not flag :
            hq.heappush(ans, (x,y))

    print(count + ans[-1][1] - ans[-1][0])


    




if __name__ == "__main__" :
    input = sys.stdin.readline
    N = int(input())
    dots = [tuple(map(int, input().split())) for _ in range(N)]

    solution(N, dots)