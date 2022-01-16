a,b=map(int,input().split())

arr=[]
for _ in range(a):
    arr.append(int(input()))

arr.sort(reverse=True)
count=0
for i in range(a):
    if b==0:
        break
    if b<arr[i]:
        continue
    else:
        count+=b//arr[i]
        b=b%arr[i]
print(count)
