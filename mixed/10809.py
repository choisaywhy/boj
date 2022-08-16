import sys
from collections import Counter

def solution(word) :
    alphabet = [-1 for _ in range(26)]
    word = word.strip()
    for i in range(len(word)):
        if alphabet[ord(word[i])-ord('a')] == -1 :
            alphabet[ord(word[i])-ord('a')] = i

    for a in alphabet :
        print(a)


word = str(sys.stdin.readline())
solution(word)