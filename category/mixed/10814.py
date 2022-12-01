import sys

N = int(sys.stdin.readline())
ages = {}
names = []

for n in range(N):
    age, name = list(map(str,sys.stdin.readline().split()))
    age = int(age)
    ages[age] = ages.get(age, []) + [n] 
    names += [name]


for age in sorted(ages.keys()) :
    for index in ages[age]:
        print(age, names[index])