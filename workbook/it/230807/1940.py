import sys

def solution():
    n = int(input())
    m = int(input())
    ing = list(map(int,input().split()))
    ans = 0
    ing.sort()

    s,e = 0,n-1
    while s < e:
        t = ing[s] + ing[e]

        if t < m:
            s += 1
        elif t > m:
            e -= 1
        else:
            ans += 1
            s += 1
            e -= 1
    print(ans)

    


if __name__ == "__main__" :
    input = sys.stdin.readline
    
    solution()




# import sys

# def solution():
#     n = int(input())
#     m = int(input())
#     tmp = list(map(int,input().split()))
#     ingredients = [False]*(max(tmp)+1)
#     l = len(ingredients)
#     ans = 0
#     for i in tmp:
#         ingredients[i] = True


#     for i in range(1, l):
#         if not ingredients[i]:
#             continue
#         if m - i >= l or m-i < i or not ingredients[m-i]:
#             continue
#         ans += 1

    
#     print(ans)


# if __name__ == "__main__" :
#     input = sys.stdin.readline
    
#     solution()
