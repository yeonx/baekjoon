import sys
N=int(sys.stdin.readline())

arr=[0]*(10000)

for _ in range(N):
    a=int(sys.stdin.readline())
    arr[a-1]+=1


for i in range(10000):
    for j in range(arr[i]):
        print(i+1)
