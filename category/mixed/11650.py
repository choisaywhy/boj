import sys

N = int(sys.stdin.readline())
dots = []

for _ in range(N):
    dots.append(list(map(int,sys.stdin.readline().split())))

for x,y in sorted(dots):
    print(x,y)