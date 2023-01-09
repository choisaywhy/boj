import sys
import re

def solution(math):
    num = re.findall('[0-9]+', math)
    exp = re.findall('\D', math)

    for i in range(len(exp)-1, -1, -1) :
        if exp[i] == '+' :
            num[i] = int(num[i]) + int(num[i+1])
            num[i+1] = 0

    res = int(num[0]) * 2
    for n in num :
        res -= int(n)
    
    print(res)




if __name__ == "__main__" :
    input = sys.stdin.readline
    math = input().strip()
    solution(math)