# str=input()

# for i in range(len(str)):
#     if str[i]>='a' and str[i]<='z':
        
st=input()
st_=[]
for i in range(len(st)):
    if st[i]>='a' and st[i]<='m':
        st_.append(chr((ord(st[i])+13)))
    elif st[i]>='n' and st[i] <='z':
        st_.append(chr((ord(st[i])-13)))
    elif st[i]>='A' and st[i]<='M':
        st_.append(chr((ord(st[i])+13)))
    elif st[i]>='N' and st[i] <='Z':
        st_.append(chr((ord(st[i])-13)))
    else:
        st_.append(st[i])

st_="".join(st_)
print(st_)
