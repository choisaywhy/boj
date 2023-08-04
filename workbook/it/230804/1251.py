import sys

def solution():
    word = list(input().strip())
    n = len(word)
    ans = []

    def dfs(idx, depth,slice):
        nonlocal ans

        if depth == 3:
            if len(slice) == n:
                ans = slice if ans == [] or ans > slice else ans
            return
        for i in range(idx+1, n+1):
            dfs(i, depth+1, slice+list(reversed(word[idx: i])))

    dfs(0,0,[])
    print("".join(ans))

if __name__ == "__main__" :
    input = sys.stdin.readline
    
    solution()



# import sys

# def solution():
#     word = list(input().strip())
#     ans = []

#     def dfs(idx, depth,slice):
#         nonlocal ans

#         if depth == 2:
#             tmp = word[:slice[0]][::-1] + word[slice[0]:slice[1]][::-1] + word[slice[1]:][::-1]
#             ans = tmp if ans == [] or ans > tmp else ans
        
#         for i in range(idx+1, len(word)):
#             dfs(i, depth+1, slice+[i])

#     dfs(0,0,[])
#     print("".join(ans))

# if __name__ == "__main__" :
#     input = sys.stdin.readline
    
#     solution()
