import sys

def solution(m,n,l):
    
    start = 1
    end = max(l)

    while start <= end:
        mid = (start + end) // 2
        # print(start,'start',end,'end',mid,'mid')


        target = 0
        for piece in l:
            target += piece // mid
        # print(target,'target')
        if target >= m:
            start = mid + 1
        else:
            end = mid - 1
        


    print(end)





if __name__ == "__main__" :
    input = sys.stdin.readline
    m,n = map(int, input().split())
    l = list(map(int, input().split()))
    solution(m,n,l)