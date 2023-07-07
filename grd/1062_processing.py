# https://www.acmicpc.net/board/view/50137 비트마스킹 풀이 참고할 것
# 시간초과

import sys
import re 

def solution():
    n,k = map(int,input().split())
    ans = 0
    words = []

    for _ in range(n):
        word = []
        for w in  list(map(str,input().strip())):
            if w in ['a','n','t','i','c'] or w in word:
                continue
            word.append(w)
            if word == "":
                ans += 1
                continue
            words.append(word)


    # for _ in range(n):
    #     word = re.sub('[antic]' ,'' ,input().strip())
    #     if word == "":
    #         ans += 1
    #         continue
    #     words.append(list(set(word)))

    if k < 5:
        print(0)
        return
    
    def dfs(depth, idx):
        nonlocal ans
        if depth == k-5:
            count = 0
            for word in words:
                for w in word:
                    if not visited[ord(w) - 97]:
                        break
                else:
                    count += 1
            if count > ans:
                ans = count
            return

        for i in range(idx, 26):
            if visited[i]:
                continue
            visited[i] = True
            dfs(depth+1, idx+1)
            visited[i] = False

    visited = [False]*26
    visited[ord('a')-97],visited[ord('n')-97],visited[ord('t')-97],visited[ord('i')-97],visited[ord('c')-97] = [True]*5
    dfs(0,0)
    print(ans)



if __name__ == "__main__" :
    input = sys.stdin.readline
    
    solution()
