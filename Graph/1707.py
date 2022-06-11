import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def DFS(v,c,ok):
    print(v,c,ok)
    for i in graph[v]:
        if color[i]==0:
            if c == 1:
                color[i]=-1
            else:
                color[i]=1
            DFS(i,color[i],ok)
        else:
            print("-----------",v,c,i,color[i])
            if c == color[i]:
                ok= -1
                DFS(i,color[i],ok)

                return ok
            else:
                return ok
        #DFS(v,color[i],ok)
    return ok

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
        
    result = DFS(1,1,1)
    
    if result == 1:
        print("YES")
    else:
        print("NO")
