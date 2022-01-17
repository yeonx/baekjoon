N=int(input())

def LCM(a,b):
    if b>a:
        a,b=b,a
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

for _ in range(N):
    a,b=map(int,input().split())
    print(a*b//LCM(b,a))

