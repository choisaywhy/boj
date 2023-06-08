## 범위 잡는 연습
# debugging
import sys

def solution(k,n,lan):

    start = 1
    end = max(lan)

    # upper index
    while start <= end:
        mid = (start + end) // 2
        
        print(start,'start',end,'end',mid,'mid')

        target = 0
        for l in lan:
            target += l // mid
        
        print(target,'target')

        if n <= target:
            start = mid + 1
            print('update start',start)
        else:
            end = mid -1
            print('update end',end)


    
    print(end)






if __name__ == "__main__" :
    input = sys.stdin.readline
    k,n = map(int, input().split())
    lan = list(int(input()) for _ in range(k))
    solution(k,n,lan)