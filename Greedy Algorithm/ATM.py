n=int(input())
arr=list(map(int,input().split()))
arr.sort()
total=0
total_arr=[]
for i in range(n):
    total_arr.append(arr[i])
    total+=sum(total_arr)
print(total)
