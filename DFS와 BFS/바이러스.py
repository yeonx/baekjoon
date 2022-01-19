import sys
from collections import deque
input=sys.stdin.readline
num=int(input())
M=int(input())

graph=[[] for _ in range(num+1)]

for _ in range(M):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visit=[False]*(num+1)
def BFS(stand):
    count=0
    q=deque([stand])
    visit[stand]=True
    while q:
        v=q.popleft()
        count+=1
        for i in graph[v]:
            if not visit[i]:
                visit[i]=True
                q.append(i)
    print(count-1)

BFS(1)
