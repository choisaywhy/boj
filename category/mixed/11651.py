import sys

N = int(sys.stdin.readline())
dots = []
dots_reverse = []

for _ in range(N):
    dots.append(list(map(int,sys.stdin.readline().split())))

for x,y in dots:
    dots_reverse.append([y,x])

for y,x in sorted(dots_reverse):
    print(x,y)