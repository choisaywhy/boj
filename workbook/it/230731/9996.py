import sys
def solution():
    n = int(input())
    start, end = input().strip().split('*')
    for _ in range(n):
        file = input().strip()
        if file.startswith(start) and file.endswith(end) and len(start)+len(end) <= len(file):
            print("DA")
            continue
        print("NE")

if __name__ == "__main__" :
    input = sys.stdin.readline
    
    solution()
