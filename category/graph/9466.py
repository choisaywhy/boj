import sys
from collections import deque

def DFS(graph,start,checked):
    stack = deque([start])
    visited = [] # 현재 탐색 경로를 지나는 node
    teams = 0
    
    while stack :
        node = stack.pop()
        if checked[node] : 
            if node in visited : 
                teams = len(visited)-visited.index(node)
                return teams, checked
            else :
                return teams, checked
        else : 
            checked[node] = True
            visited.append(node)
            stack.extend(graph[node])


input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    arr = list(map(int,input().split()))
    graph = {}

    for i in range(N): # graph 생성
        graph[i+1] = [arr[i]]

    checked = [False for _ in range(N+1)] # 경로 탐색이 완료된 node = True else False
    team = 0
    for start in range(1,N+1):
        if not checked[start] : # 검증하지 않은 노드만 DFS
            teams, checked = DFS(graph,start,checked)
            team += teams # 팀원 수 세기
    print(N-team)
    
    

# import sys
# from collections import deque

# def DFS(graph,start,checked):
#     stack = deque([start])
#     visited = []
#     teams = 0

#     while stack :
#         node = stack.pop()
#         if checked[node] :
#             for v in set(visited):
#                 checked[v] = True
#             return teams, checked
#         if node not in visited :
#             visited.append(node)
#             stack.extend(graph[node])
#         else :
#             for v in set(visited):
#                 checked[v] = True
#             teams = len(visited)-visited.index(node)
#             return teams, checked


# input = sys.stdin.readline
# T = int(input())

# for _ in range(T):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     graph = {}

#     for i in range(N):
#         graph[i+1] = [arr[i]]

#     checked = [False for _ in range(N+1)]
#     team = 0
#     for start in range(1,N+1):
#         if checked[start] :
#             continue
#         teams, checked = DFS(graph,start,checked)
#         team += teams
#     print(N-team)


# import sys
# from collections import deque

# def DFS(graph,start,checked,teams):
#     stack = deque([start])
#     visited = []

#     while stack :
#         node = stack.pop()
#         if checked[node] :
#             for v in set(visited):
#                 checked[v] = True
#             return teams, checked
#         if node not in visited :
#             visited.append(node)
#             stack.extend(graph[node])
#         else :
#             for v in set(visited):
#                 checked[v] = True
#             for t in set(visited[visited.index(node):]):
#                 teams[t] = True
#             return teams, checked


# input = sys.stdin.readline
# T = int(input())

# for _ in range(T):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     graph = {}

#     for i in range(N):
#         graph[i+1] = [arr[i]]

#     checked = [False for _ in range(N+1)]
#     teams = [False for _ in range(N+1)]
#     count = 0
#     for start in range(1,N+1):
        
#         if checked[start] :
#             print(start,'already checked')
#             continue
#         teams, checked = DFS(graph,start,checked,teams)
#     for c, t in zip(checked, teams):
#         if c != t :
#             count+= 1
#     print(count)







# import sys
# from collections import deque
# def DFS(graph,start,visiting):
#     stack = deque()
#     visited = []
#     stack.append(start)

#     while stack :
#         node = stack.pop()
#         if node not in visited :
#             visited.append(node)
#             stack.extend(graph[node])
#         else :
#             if node in visiting:
#                 return set(visited), []
#             teams = set(visited[visited.index(node):])
#             print("dfs started and found teams :",teams,'and visited :',visited)
#             return set(visited),teams

# input = sys.stdin.readline
# T = int(input())

# for _ in range(T):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     graph = {}
#     count = 0

#     for i in range(N):
#         graph[i+1] = [arr[i]]
    
#     team = [False for _ in range(N+1)]
#     visiting = set()
#     for start in range(1,N+1):
#         print('exploring ',start)
#         if start in visiting or team[start]:
#             print(start,'already checked')
#             continue
#         if graph[start][0] in visiting or team[graph[start][0]] :
#             print('destination already taken')
#             visited.add(start)
#             count += 1
#             print('count updated :', count)
#             continue
#         visited,teams = DFS(graph, start,visiting)

#         for t in teams :
#             team[t] = True
#         print('team updated :',team)
#         count += len(visited) - len(teams)
#         print(count,"count")
#         visiting |= visited
#         print('visiting updated',visiting)

#     print(count)




# import sys
# from collections import deque
# def DFS(graph,start):
#     stack = deque()
#     visited = []
#     stack.append(start)

#     while stack :
#         node = stack.pop()
#         if node not in visited :
#             visited.append(node)
#             stack.extend(graph[node])
#         else :
#             loser = visited[:visited.index(node)]
#             visiting = visited[visited.index(node):]
#             return visiting,loser

# input = sys.stdin.readline
# T = int(input())

# for _ in range(T):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     graph = {}
#     count = 0

#     for i in range(N):
#         graph[i+1] = [arr[i]]
    
#     team = [False for _ in range(N+1)]
#     fails = [False for _ in range(N+1)]
#     for start in range(1,N+1):
#         if fails[graph[start][0]]:
#             count += 1
#             continue
#         if team[start] :
#             continue
#         visiting,loser = DFS(graph, start)
#         for v in visiting :
#             team[v] = True
#         for l in loser :
#             count += 1
#             fails[l] = True
            
        
#     print(count)







# import sys
# from collections import deque
# def DFS(graph,start):
#     stack = deque()
#     visited = []
#     stack.append(start)

#     while stack :
#         node = stack.pop()
#         if node not in visited :
#             visited.append(node)
#             stack.extend(graph[node])
#         else :
#             if node == start :
#                 return True, visited
#     return False, visited

# input = sys.stdin.readline
# T = int(input())

# for _ in range(T):
#     N = int(input())
#     arr = list(map(int,input().split()))
#     graph = {}
#     count = 0

#     for i in range(N):
#         graph[i+1] = [arr[i]]
    
#     team = [False for _ in range(N+1)]
#     for start in range(1,N+1):
#         if team[start] :
#             print(start,'already checked')
#             continue
#         check, visiting = DFS(graph, start)
#         if check :
#             for v in visiting :
#                 team[v] = True
#         else :
#             count += 1

#     print(count)

