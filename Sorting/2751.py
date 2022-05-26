import sys

n=int(sys.stdin.readline())

sorting=[]
for i in range(n):
    sorting.append(int(sys.stdin.readline()))
sorting.sort()
for i in range(n):
    print(sorting[i])
