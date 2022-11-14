import sys

input = sys.stdin.readline

def star(N):
    if N == 3:
        pattern = [[" ", " ", "*", " ", " "],
                   [" ", "*", " ", "*", " "],
                   ["*", "*", "*", "*", "*"]]
        return pattern

    div2 = N//2
    pattern = star(div2)
    new_pattern = [[" "]*(2*N - 1) for _ in range(N)]

    for i in range(div2) :
        new_pattern[i][div2 : div2 + N-1] = pattern[i]
    for i in range(div2, N) :
        new_pattern[i] = pattern[i-div2] + [" "] + pattern[i-div2]
    
    return new_pattern

N = int(input()) # 3*2^k

pattern = star(N)
result = ""
for i in range(len(pattern)) :
    result += "".join(pattern[i]) + "\n"


sys.stdout.write(result.rstrip())
