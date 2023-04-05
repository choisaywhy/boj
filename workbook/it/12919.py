# T->S 방식
import sys

def solution(S, T):
    flag = False

    def DFS(temp):
        nonlocal flag

        if len(temp) == len(S):
            if temp == S:
                flag = True
            return
        
        if temp[0] == 'B': # B소거
            DFS(temp[-1:0:-1])
        if temp[-1] == 'A':
            DFS(temp[:-1])

    DFS(T)
    print(1 if flag else 0)


if __name__ == "__main__" :
    input = sys.stdin.readline
    S = input().strip()
    T = input().strip()
    solution(S, T)


# S에서 A,B를 붙여 T를 만드는 방식 -> 시간 초과
# import sys

# def solution(S, T):
#     ta, tb = T.count('A'), T.count('B')
#     countA, countB = S.count('A'), S.count('B')
#     flag = False

#     def DFS(temp, reversed):
#         nonlocal countA, countB, flag
#         if countA > ta or countB > tb:
#             return
#         if len(temp) == len(T):
#             temp = temp[::-1] if reversed else temp
#             if temp == T:
#                 flag = True
#             return
        
#         if not reversed:
#             countA += 1
#             DFS(temp + 'A', reversed)
#             countA -= 1
#             countB += 1
#             DFS(temp + 'B', not reversed)
#             countB -= 1
#         else:
#             countA += 1
#             DFS('A' + temp, reversed)
#             countA -= 1
#             countB += 1
#             DFS('B' + temp, not reversed)
#             countB -= 1

#     DFS(S, False)
#     print(1 if flag else 0)


# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     S = input().strip()
#     T = input().strip()
#     solution(S, T)




# debugging ver
# import sys

# def solution(S, T):
#     count = (T.count('A'), T.count('B'))
#     countA, countB = 0, 0
#     flag = False

#     def DFS(temp, depth, reversed):
#         nonlocal countA, countB, flag
#         print(temp, depth, reversed, 'turn')
#         if countA > count[0] or countB > count[1]:
#             print('A나 B개수 초과, 백트레킹')
#             return
#         if depth == len(T):
#             print('길이 도달')
#             if reversed:
#                 if temp[::-1] == T:
#                     print('정답과 같음')
#                     flag = True
#             if temp == T:
#                 flag = True
#             return
        
#         if not reversed:
#             countA += 1
#             DFS(temp + 'A', depth+1, reversed)
#             countA -= 1
#             countB += 1
#             DFS(temp + 'B', depth+1, not reversed)
#             countB -= 1
#         else:
#             countA += 1
#             DFS('A' + temp, depth+1, reversed)
#             countA -= 1
#             countB += 1
#             DFS('B' + temp, depth+1, not reversed)
#             countB -= 1

#     DFS(S, len(S), False)
#     print(1 if flag else 0)




# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     S = input().strip()
#     T = input().strip()
#     solution(S, T)