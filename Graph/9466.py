import sys
sys.setrecursionlimit(11111111)
input = sys.stdin.readline

def DFS(num):
    global cnt
    vis[num]=1
    next=graph[num]
    if vis[next]==0:
        DFS(next)
    elif done[next]==0:
        i=next
        while True:
            if i==num:
                break
            cnt+=1
            i=graph[i]
        cnt+=1
    done[num]=1

T = int(input())

for _ in range(T):
    n = int(input())
    arr=list(map(int,input().split()))
    done = [0 for _ in range(n+1)]
    graph = [0]

    for i in range(n):
        graph.append(arr[i])

    vis = [0 for _ in range(n+1)]

    cnt=0
    for i in range(1,n+1):
        if vis[i]==0:
            DFS(i)
    print(n-cnt)
