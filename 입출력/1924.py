month=[31,28,31,30,31,30,31,31,30,31,30,31]
whatday=["SUN","MON","TUE","WED","THU","FRI","SAT"]

x,y=map(int,input().split())

day=y

for i in range(x-1):
    day+=month[i]

print(whatday[day%7])
