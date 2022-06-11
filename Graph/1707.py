import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(v,c):
    if c==0:
        c=1
    for i in graph[v]:
        if color[i]==0:
            if c == 1:
                color[i]=-1
            else:
                color[i]=1
            a=DFS(i,color[i])
            if not a:
                return False
        elif c == color[i]:
            return False
    return True

k=int(input())

for _ in range(k):
    v,e=map(int,input().split())
    
    graph = [[] for _ in range(v+1)]
    color = [0]*(v+1)
    for _ in range(e):
        a,b= map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    for i in range(1,v+1):
        graph[i].sort()
        
    for i in range(1,v+1):
        if color[i]==0:
            ok = DFS(i,color[i])
            if ok is False:
                break
    if ok == True:
        print("YES")
    else:
        print("NO")
