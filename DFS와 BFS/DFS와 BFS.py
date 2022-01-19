
import sys
from collections import deque
input=sys.stdin.readline
N,M,V=map(int,input().split())

v=[[] for _ in range(N+1)]

for _ in range(M):
    a,b=map(int,input().split())
    v[a].append(b)
    v[b].append(a)
for i in range(N):
    v[i+1].sort()
visit=[False]*(N+1)
def DFS(V):
    visit[V]=True
    print(V,end=' ')
    for x in v[V]:
        if visit[x]!=True:
            DFS(x)

DFS(V)
print("")
visit=[False]*(N+1)
def BFS(V):
    q=deque([V])
    visit[V]=True
    
    while q:
        k=q.popleft()
        print(k,end=' ')
        for i in v[k]:
            if not visit[i]:
                q.append(i)
                visit[i]=True

BFS(V)
