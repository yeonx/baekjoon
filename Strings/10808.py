str=input()

count=[0]*26
for i in range(len(str)):
    count[ord(str[i])-ord('a')]+=1

for i in range(26):
    print(count[i],end=' ')
