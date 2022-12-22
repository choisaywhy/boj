import sys

def solution(T):
    def fibonacci(n) :
        nonlocal zero, one
        if n == 0 :
            zero += 1
            return 0
        elif n == 1 :
            one += 1
            return 1
        else :
            return fibonacci(n-1) + fibonacci(n-2)



    for _ in range(T) :
        zero, one = 0, 0
        fibonacci(int(input()))
        print(zero, one)





if __name__ == "__main__" :
    input = sys.stdin.readline
    T = int(input())

    solution(T)