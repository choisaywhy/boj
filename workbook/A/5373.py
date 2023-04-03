# 현재 윗면을 나타내는 target이 필요
# cube = [["w","w","w"] ... ]
# cube_side = {"U":0, "D":1 ...}
# 방향은 맞으니 directions 는 유지

import sys

def solution(turning):
    cube = { "U": [["w"]*3 for _ in range(3)], 
             "D": [["y"]*3 for _ in range(3)], 
             "F": [["r"]*3 for _ in range(3)], 
             "B": [["o"]*3 for _ in range(3)], 
             "L": [["g"]*3 for _ in range(3)], 
             "R": [["b"]*3 for _ in range(3)]}
    
    side_switch = { "U": {"U":"U", "D":"D", "F":"F", "B":"B", "L":"L", "R":"R"}, 
                    "D": {"U":"D", "D":"U", "F":"F", "B":"B", "L":"R", "R":"L"}, 
                    "F": {"U":"F", "D":"B", "F":"D", "B":"U", "L":"L", "R":"R"}, 
                    "B": {"U":"B", "D":"F", "F":"D", "B":"U", "L":"R", "R":"L"}, 
                    "L": {"U":"L", "D":"R", "F":"D", "B":"U", "L":"B", "R":"F"}, 
                    "R": {"U":"R", "D":"L", "F":"D", "B":"U", "L":"F", "R":"B"}}

    # 회전 방향 clockwise, (side, 가로:True 세로:False, index, reversed:True, False )
    directions = { "U": [("B", True, 0, True), ("R", True, 0, True), ("F", True, 0, True), ("L", True, 0, True)], 
                   "D": [("L", True, 2, True), ("F", True, 2, True), ("R", True, 2, True), ("B", True, 2, True)], 
                   "F": [("R", False, 0, True), ("D", True, 2, True), ("L", False, 2, False), ("U", True, 2, True)], 
                   "B": [("U", True, 0, True), ("L", False, 0, False), ("D", True, 0, True), ("R", False, 2, True)], 
                   "L": [("U", False, 0, True), ("F", False, 0, True), ("D", False, 2, False), ("B", False, 2, False)], 
                   "R": [("B", False, 0, True), ("D", False, 0, True), ("F", False, 2, False), ("U", False, 2, False)]}
    

    
    def swap(direction, side):

        preside, prelr, preidx, prerev = direction[0]
        preside = side_switch[side][preside]
        pretemp = cube[preside][preidx] if prelr else list(cube[preside][j][preidx] for j in range(3))

        for i in range(1,4):
            curside, curlr, curidx, currev = direction[i]
            curside = side_switch[side][curside]
            curtemp = cube[curside][curidx] if curlr else list(cube[curside][j][curidx] for j in range(3))
            if currev != prerev:
                pretemp = pretemp[::-1]
            if curlr:
                cube[curside][curidx] = pretemp
            else:
                for j in range(3):
                    cube[curside][j][curidx] = pretemp[j]
            
            pretemp = curtemp
            prerev = currev
            preside = curside
        
        curside, curlr, curidx, currev = direction[0]
        curside = side_switch[side][curside]

        if currev != prerev:
            pretemp = pretemp[::-1]
        if curlr:
            cube[curside][curidx] = pretemp
        else:
            for j in range(3):
                cube[curside][j][curidx] = pretemp[j]
            
    for turn in turning:
        side, dir = turn[0], True if turn[1] == "+" else False
        print(side, dir,'turn----------------------------------------------------------')
        if dir:
            swap(directions[side], side)
        else:
            swap(directions[side][::-1], side)
    #     print('cube updated',cube)
    # print('final cube',cube)
    print(cube["U"])
        


if __name__ == "__main__" :
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        turns = int(input())
        turning = list(input().strip().split())
        solution(turning)


# debugginf ver
# import sys

# def solution(turning):
#     cube = { "U": [["w"]*3 for _ in range(3)], 
#              "D": [["y"]*3 for _ in range(3)], 
#              "F": [["r"]*3 for _ in range(3)], 
#              "B": [["o"]*3 for _ in range(3)], 
#              "L": [["g"]*3 for _ in range(3)], 
#              "R": [["b"]*3 for _ in range(3)]}
#     directions = { "U": [("B", True, 0), ("R", True, 0), ("F", True, 0), ("L", True, 0)],  # 가로:True 세로:False
#                    "D": [("L", True, 0), ("F", True, 0), ("R", True, 0), ("B", True, 0)], 
#                    "F": [("R", False, 0), ("D", False, 0), ("L", False, 2), ("U", True, 2)], 
#                    "B": [("U", True, 0), ("L", False, 0), ("D", False, 2), ("R", False, 2)], 
#                    "L": [("U", False, 0), ("F", False, 0), ("D", True, 2), ("B", False, 2)], 
#                    "R": [("B", False, 0), ("D", True, 0), ("F", False, 2), ("U", False, 2)]}
    
#     def swap(direction):
#         preside, prelr, preidx = direction[0]
#         pretemp = cube[preside][preidx] if prelr else list(cube[preside][j][preidx] for j in range(3))

#         for i in range(1,4):
#             curside, curlr, curidx = direction[i]
#             curtemp = cube[curside][curidx] if curlr else list(cube[curside][j][curidx] for j in range(3))
#             if curlr:
#                 cube[curside][curidx] = pretemp
#             else:
#                 for j in range(3):
#                     cube[curside][j][curidx] = pretemp[j]
            
#             pretemp = curtemp
        
#         curside, curlr, curidx = direction[0]
#         if curlr:
#             cube[curside][curidx] = pretemp
#         else:
#             for j in range(3):
#                 cube[curside][j][curidx] = pretemp[j]


#     for turn in turning:
#         side, dir = turn[0], True if turn[1] == "+" else False
#         print("side","dir",turn)
#         if dir:
#             swap(directions[side])
#         else:
#             swap(directions[side][::-1])
#         print("updated cube",cube)

#     print(cube["U"])
        







# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     T = int(input())
#     for _ in range(T):
#         turns = int(input())
#         turning = list(input().strip().split())
#         solution(turning)