import sys

def solution(arr):
    for num in arr :
        if num == num[::-1] :
            print("yes")
        else:
            print("no")


if __name__ == "__main__" :
    input = sys.stdin.readline
    arr = []
    while True :
        temp = str(input().strip())
        if temp == '0' :
            break
        arr.append(temp)
    solution(arr)