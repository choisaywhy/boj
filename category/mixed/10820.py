import sys

def solution(word) :
    small, big, num, space = 0,0,0,0

    for w in word :
        if ord(w) >=48 and ord(w) <=57 :
            num += 1
        elif ord(w) >=97 and ord(w) <=122 :
            small += 1
        elif ord(w) >=65 and ord(w) <=90 :
            big += 1
        elif ord(w) == 32 :
            space += 1
    print(small, big, num, space)
    return 0


while True :
    try :
        word = str(input())
        solution(word)
    except EOFError: # sys.stdin.read()는 공백, input()는 EOFError을 일으킨다
        break