import sys

input = sys.stdin.readline

def quad_tree(N, x, y) :
    if N == 1:
        return data[x][y]

    div2 = N//2

    LT = quad_tree(div2, x, y)
    RT = quad_tree(div2, x, y+div2)
    LB = quad_tree(div2, x+div2, y)
    RB = quad_tree(div2, x+div2, y+div2)

    if LT == RT == LB == RB and len(LT) == 1:
        return LT
    else :
        return "("+LT+RT+LB+RB+")"
    

N = int(input())
data = [[d for d in str(input().strip())] for _ in range(N)]

result = quad_tree(N, 0,0)

print(result)
# print(result)

# import sys

# input = sys.stdin.readline

# def quad_tree(N, x, y) :
#     if N == 2:
#         if data[x][y] == data[x][y+1] == data[x+1][y] == data[x+1][y+1] :
#             return [data[x][y]]
#         else :
#             return ["(", data[x][y], data[x][y+1], data[x+1][y], data[x+1][y+1],")"]

#     div2 = N//2

#     LT = quad_tree(div2, x, y)
#     RT = quad_tree(div2, x, y+div2)
#     LB = quad_tree(div2, x+div2, y)
#     RB = quad_tree(div2, x+div2, y+div2)

#     if LT == RT == LB == RB and len(LT) == 1:
#         result.append(LT)
#     else :
#         result.extend(LT+RT+LB+RB)
    




# N = int(input())
# data = [[d for d in str(input().strip())] for _ in range(N)]
# result = []

# quad_tree(N, 0,0)

# print("".join(result))