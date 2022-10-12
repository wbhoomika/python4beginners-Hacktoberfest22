st=input("Enter a string: ")
ch=input("Enter a character: ")
leng=len(st)
ctr=0

for i in range(0,leng):
    current=st[i]
    if current==ch:
        ctr+=1

print(ch,"is in the string",ctr,"times")
