st=input()

st_li=[]

for i in range(len(st)):
    st_li.append(st[i:])
    

st_li.sort()

for i in st_li:
    print(i)
