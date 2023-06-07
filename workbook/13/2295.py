import sys

def solution(n,u):
    
    t = [u[x]+u[y] for x in range(n) for y in range(x,n)]
    
    u.sort()
    t.sort()
    flag = False
    for l in range(n-1,-1,-1): # u + v + w
        for w in range(n): # w

            start = 0
            end = len(t)-1
            target =  u[l] - u[w]
            while start < end:
                mid = (start + end) // 2

                if t[mid] < target:
                    start = mid + 1
                else:
                    end = mid
            
            if t[start] != target:
                continue
            flag = True
            break

        if flag:
            print(u[l])
            break
            


if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    u = [int(input()) for _ in range(n)]
    solution(n,u)