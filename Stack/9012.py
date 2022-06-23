n = int(input())

for _ in range(n):
    stack=[]
    what = input()
    fg=0
    for i in range(len(what)):
        if what[i]=='(':
            stack.append(1)
        else:
            if len(stack)==0:
                print("NO")
                fg=1
                break
            else:
                stack.pop()
    if fg==0:
        if len(stack) != 0:
            print("NO")
        else:
            print("YES")
