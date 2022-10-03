N=int(input())
n_c = str(N)

total = 0
number = []
for i in range(len(n_c)) : 
    total+=int(n_c[i])
    number.append(n_c[i])
number.sort()
number.reverse()
answer=''
for i in range(len(number)):
        answer+=number[i]
k=int(answer)
if k%30 !=0:
    print(-1)
else:
    print(k)
