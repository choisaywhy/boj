import sys
from collections import Counter

def solution(word) :
    answer = ""

    for w in word:
        code = ord(w)
        ROT13 = 0
        if code >= ord('a') and code <= ord('z') :
            ROT13 = ord(w) + 13
            if ROT13 > ord('z'):
                ROT13 = ROT13 - ord('z') + ord('a') - 1
        elif code >= ord('A') and code <= ord('Z') :
            ROT13 = ord(w) + 13
            if ROT13 > ord('Z'):
                ROT13 = ROT13 - ord('Z') + ord('A') - 1
        else :
            answer += w
            continue
        answer += chr(ROT13)

    return answer


word = str(sys.stdin.readline().rstrip('\n'))
print(solution(word))
