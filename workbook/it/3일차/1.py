import sys
from collections import Counter
def solution(word):
    count = Counter(word)
    ans = []
    for k, v in count.items():
        ans.append((v,k))
    
    ans.sort(reverse=True)
    if len(ans) >1 and ans[0][0] == ans[1][0]:
        print("?")
    else:
        print(ans[0][1])





if __name__ == "__main__" :
    input = sys.stdin.readline
    word = input().strip().upper()
    solution(word)