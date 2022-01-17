a,b=map(int,input().split())

arr1=[]
for i in range(1,a+1):
    if a%i==0:
        arr1.append(i)

arr2=[]
for i in range(1,b+1):
    if b%i==0:
        arr2.append(i)

arr3=[]
for i in arr1:
    if i in arr2:
        arr3.append(i)

print(arr3[-1])

A=a//arr3[-1]
B=b//arr3[-1]

print(A*B*arr3[-1])

