str=input()

for i in range(len(str)):
    if i%10==9:
        print(str[i])
    else:
        print(str[i],end="")
