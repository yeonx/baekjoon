import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m=map(int,input().split())

count=0

graph = [[] for _ in range(n+1)]

for _ in range(m) :
    a,b=map(int,input().split())
    1
    graph[a].append(b)
    graph[b].append(a)

for i in range(1,n+1):
    graph[i].sort()

vis=[False]*(n+1)
def dfs(v):
    vis[v]=True
    for i in graph[v] :
        if not vis[i]:
            dfs(i)

for i in range(1,n+1):
    if not vis[i]:
        count+=1
        dfs(i)

print(count)
