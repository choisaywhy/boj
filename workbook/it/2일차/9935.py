import sys

def solution(ss, bomb):
    ans = []

    while ss:
    
        ans.append(ss.pop())
        if len(ans) < len(bomb):
            continue
        
        if bomb == ans[len(ans)-len(bomb):]:
            for _ in range(len(bomb)):
                ans.pop()
        
            
    if ans == []:
        print("FRULA")
    else:
        print("".join(ans))




if __name__ == "__main__" :
    input = sys.stdin.readline
    ss = list(map(str, input().strip()))[::-1]
    bomb = list(map(str, input().strip()))
    solution(ss, bomb)



#debugging
# import sys

# def solution(ss, bomb):
#     ans = []

#     while ss:
    
#         ans.append(ss.pop())
#         print(ans,'updated')
#         if len(ans) < len(bomb):
#             continue
        
#         print('slivce', ans[len(ans)-len(bomb):])
#         if bomb == ans[len(ans)-len(bomb):]:
#             for _ in range(len(bomb)):
#                 ans.pop()
        
            
#     if ans == []:
#         print("FRULA")
#     else:
#         print("".join(ans))






# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     ss = list(map(str, input().strip()))[::-1]
#     bomb = list(map(str, input().strip()))
#     solution(ss, bomb)