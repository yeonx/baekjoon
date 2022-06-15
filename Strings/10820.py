def count(st):
    
    fg=0
    s,b,n,t=0,0,0,0
    
    for i in range(len(st)):
        if st[i]==' ':
            t+=1
        elif st[i]>='0' and st[i]<='9':
            n+=1
        elif st[i]>='a' and st[i]<='z':
            s+=1
        elif st[i]>='A' and st[i]<='Z':
            b+=1
        else:
            fg=1
    if fg==1:
        return -1,-1,-1,-1
    else:
        return s,b,n,t

str = []
while (True):
    try:
        str=input()
        s,b,n,t= count(str)
        if s==0 and b==0 and n==0 and t==0:
            break
        print(s,b,n,t)
    except EOFError:
        break


'''
This is String
SPACE    1    SPACE
 S a M p L e I n P u T     
0L1A2S3T4L5I6N7E8
'''
