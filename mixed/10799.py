import sys

def solution(steels) :
    pipe = 0
    pieces = 0
    flag = False

    for s in range(len(steels)) :
        if steels[s] == '(' :
            if steels[s+1] == ')':
                pieces += pipe
                flag = True
            else :
                pieces += 1
                pipe += 1
        else :
            if flag:
                flag = False
                continue
            else:
                pipe -= 1 
    return pieces

    




steels = str(sys.stdin.readline())
print(solution(steels))