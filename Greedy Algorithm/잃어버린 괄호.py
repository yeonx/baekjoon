arr=input()

ma=0
pl=0
su=""
flag=0
for i in range(len(arr)+1):
    if i==len(arr):
        cnt=int(su)
        if flag==1:
            ma+=cnt
        else:
            pl+=cnt

    elif arr[i]=='-' or arr[i]=='+':
        cnt=int(su)
        su=""
        if flag==1:
            ma+=cnt
        else:
            pl+=cnt
        if arr[i]=='-':
            flag=1
    else:
        su+=arr[i]

print(pl-ma)
