import sys

A, B = map(int,sys.stdin.readline().split())
m = int(sys.stdin.readline())
array = list(map(int,sys.stdin.readline().split()))
a_10 = ""
for a in array:
    if a >= 10 :
        a_10 += chr(ord('A') + int(a) - 10)
    else :
        a_10 += str(a)

base = []
a_10 = int(a_10, A)
while a_10 > 0:
    a_10, mod = divmod(a_10,B)
    base.append(mod)

print(" ".join(map(str,base[::-1])))
