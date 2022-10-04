import sys
input = sys.stdin.readline

def devi(start_i, start_j, size):
    if size == 1:
        print(arr[start_i][start_j],end="")
        return
    num = arr[start_i][start_j]
    
    for i in range(start_i,start_i + size):
        for j in range(start_j,start_j+size):
            if num != arr[i][j]:
                print("(",end="")
                size = size // 2
                devi(start_i,start_j,size)
                devi(start_i,start_j + size,size)
                devi(start_i + size ,start_j,size)
                devi(start_i + size ,start_j + size ,size)
                print(")",end="")
                return
    
    print(arr[start_i][start_j],end="")

    return


n = int(input())
arr = []

for _ in range(n) : 
    arr.append(list(map(int, list(input().rstrip()))))

devi(0,0,n)
