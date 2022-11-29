import sys
import re

def solution():
    strs = []
    while True :
        tmp = input().rstrip()
        if tmp == "." :
            break
        strs.append(re.sub('[^\[\]\(\)]','',tmp))

    for blanket in strs :
        if not blanket :
            print("yes")
            continue
        
        stack = []
        flag = True
        for b in blanket :
            if b == "(" or b == "[" :
                stack.append(b)
            elif b == ")" :
                if not stack or stack.pop() != "(":
                    flag = False
                    break
            elif b == "]" :
                if not stack or stack.pop() != "[":
                    flag = False
                    break
        if flag and not stack : # 초기 코드 flag만 --> 반례 ()( , 열리고 나서 닫히지 않은 괄호도 고려해야하기 때문
            print("yes")
        else:
            print("no")




if __name__ == "__main__" :
    input = sys.stdin.readline
    solution()
    