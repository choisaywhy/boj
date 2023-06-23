import sys

def solution(n,words):
    level = {}

    for word in words:
        for i in range(len(word)):
            level[word[i]] = level.get(word[i], 0) + 10**(len(word) - i - 1)
    sub = sorted(level.items(), key=lambda x : x[1], reverse=True)

    num = 9
    ans = 0
    for k, v in sub:
        ans += num*v
        num -= 1

    print(ans)
            

if __name__ == "__main__" :
    input = sys.stdin.readline
    n = int(input())
    words = [str(input().strip()) for _ in range(n)]
    solution(n,words)

    


# first trial
# 최대 자리수가 전체 자리수 동태를 반영 못함
# import sys

# def solution(n,words):
#     level = {}
#     sub = {}

#     for word in words:
#         for i in range(len(word)):
#             if level.get(word[i],False):
#                 level[word[i]][1] += 1
#                 if level[word[i]][0] < len(word) - i:
#                     level[word[i]][0] = len(word) - i
#             else:
#                 level[word[i]] = [len(word) - i, 1]
#             if level[word[i]][1] > 10:
#                 level[word[i]][0] += 1
#                 level[word[i]][1] -= 10
#     print(level)
#     num = 9
#     for val in sorted(list(level.values()), reverse=True):
#         for k, v in level.items():
#             if val != v:
#                 continue
#             sub[k] = num
#             num -= 1
#             level[k] = 0
#     ans = 0

#     for word in words:
#         exchange = 0
#         for i in range(len(word)):
#             exchange += sub[word[i]] * 10**(len(word) - i-1)
        
#         ans += exchange
#     print(sub)
#     print(ans)
            

    



# if __name__ == "__main__" :
#     input = sys.stdin.readline
#     n = int(input())
#     words = [str(input().strip()) for _ in range(n)]
#     solution(n,words)

    