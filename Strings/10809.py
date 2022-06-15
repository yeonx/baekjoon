str=input()

count=[-1]*26
for i in range(len(str)):
    if count[ord(str[i])-ord('a')] == -1:
        count[ord(str[i])-ord('a')]=i

for i in range(26):
    print(count[i],end=' ')
