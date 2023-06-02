import sys

def solution(string):
    
    stack = []

    for s in string:
        stack.append(s)

        if len(stack) >= 4 and stack[-1:-5:-1] == ["P","A","P","P"]:
            for _ in range(4):
               stack.pop()
            stack.append("P")
            
    if stack == ["P"]:
        print("PPAP")
    else:
        print("NP")        




if __name__ == "__main__" :
    input = sys.stdin.readline
    string = input().strip()
    solution(string)