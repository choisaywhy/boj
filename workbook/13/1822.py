import sys

def solution(n,m,a,b):
    
    ans = []
    a.sort()
    b.sort()

    for target in a:
        start = 0
        end = m-1
        flag = True

        while start <= end:
            
            mid = (start + end) // 2


            if target > b[mid]:
                start = mid + 1
            elif target < b[mid]:
                end = mid - 1
            else:
                flag = False
                break
        
        if flag:
            ans.append(target)

    print(len(ans))
    print(" ".join(map(str, ans)))


if __name__ == "__main__" :
    input = sys.stdin.readline
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    solution(n,m,a,b)



# by set
# import sys

# def solution(n,m,a,b):
    
#     ans = list(set(a) - set(b))
#     ans.sort()

#     print(len(ans))
#     print(" ".join(map(str, ans)))




