import sys

N = int(sys.stdin.readline())


students = []
for n in range(N) :
    name, k, e, m = list(map(str,sys.stdin.readline().split()))
    k, e, m = int(k), int(e), int(m)
    students.append([name,k,e,m])

students.sort(key = lambda x: (-x[1],x[2],-x[3],x[0]))

for student in students:
    print(student[0])




# class 시도의 흔적
# class Student :

#     def __init__(self, name, korean, english, math):
#         self.name = name
#         self.korean = korean
#         self.english = english
#         self.math = math
    
#     def __repr__(self) :
#         return self.name +' ' + str(self.korean) +' ' + str(self.english) + ' ' +str(self.math)

    
#     def __lt__(self, other):
        
#         if self.korean > other.korean : 
#             return self.name
#         elif self.korean == other.korean :
#             if self.english < other.english:
#                 return self.name
#             elif self.english == other.english :
#                 if self.math > other.math:
#                     return self.name
#                 elif self.math == other.math:
#                     if ord(self.name) < ord(other.name):
#                         return self.name
#         return other.name