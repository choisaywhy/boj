import sys
from collections import Counter
def solution(str1, str2):
    len1 = len(str1) 
    len2 = len(str2)

    dp = [[0]*(len2+1) for _ in range(len1+1)]
    
    for x in range(len1) :
        for y in range(len2) :
            if str1[x] == str2[y] :
                dp[x+1][y+1] = dp[x][y] + 1
            else :
                dp[x+1][y+1] = max(dp[x+1][y], dp[x][y+1])
    print(dp[-1][-1])  
    


if __name__ == "__main__" :
    input = sys.stdin.readline
    str1 = str(input().strip())
    str2 = str(input().strip())
    solution(str1, str2)