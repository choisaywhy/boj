import sys
from collections import Counter

def solution(word) :
    alphabet = [0 for _ in range(26)]
    count = Counter(word.strip())

    for key, item in count.items():
        alphabet[ord(key)-ord('a')] = item

    for a in alphabet :
        print(a)




word = str(sys.stdin.readline())
solution(word)