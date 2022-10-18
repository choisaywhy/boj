import sys

# 1
def solution(S):
    if sorted(S) == S :
        return True
    else :
        return False


# 2
def solution2(S) :
    if len(set(S)) == 1:
        return True
    flag = False
    for l in S :
        if flag :
            if l == 'a':
                return False
        if l == 'b' :
            flag = True
    return True
