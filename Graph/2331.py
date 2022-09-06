A,P = map(int, input().split())

arr = []
arr.append(A)


while True:
    arr_add=0
    while True:
        p=1
        for i in range(P):
            p=(A%10)*p
        arr_add += p
        A = A//10
        if A==0:
            A = arr_add
            break

    if arr_add in arr:
        for i in range(9999):
            if arr[i]==arr_add:
                break
        print(i)
        break
    arr.append(arr_add)
