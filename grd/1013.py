import sys
import re
def solution():
    if re.fullmatch('(100+1+|01)+', input().strip()) == None:
        print("NO")
    else:
        print("YES")



if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    for _ in range(n):
        solution()
