n=int(input())
arr=[]

for _ in range(n):
    a,b=map(int,input().split())
    if b>=a:
        arr.append((a,b))

arr.sort(key=lambda x:x[1])
i=1
cnt=0
tmp=[]
while True:
    if i==n:
        if len(tmp)!=0:
            end=i
            k=0
            tmp.sort(key=lambda x:x[0])
            #print('sort : ',tmp)
            for j in range(st,end):
                arr[j]=tmp[k]
                k+=1
            tmp=[]
        break
    if arr[i-1][1]==arr[i][1]:
        if len(tmp)==0:
            st=i-1
            tmp.append(arr[i-1])
        tmp.append(arr[i])
        #print(tmp, len(tmp))
    else:
        if len(tmp)!=0:
            end=i
            k=0
            tmp.sort(key=lambda x:x[0])
            #print('sort : ',tmp)
            for j in range(st,end):
                arr[j]=tmp[k]
                k+=1
            tmp=[]
        st=-1
        end=-1
    i+=1

#print('arr : ',arr)
cnt=1
stard=arr[0][1]
i=1
while i<n:
    if arr[i][0]>=stard:
        cnt+=1
        stard=arr[i][1]
    i+=1

print(cnt)
