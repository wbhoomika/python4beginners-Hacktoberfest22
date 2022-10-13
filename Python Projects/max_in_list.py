x=int(input("How many entries: "))
li=[]
for i in range(x):
    li.append(int(input()))
max=0
for i in li:
    if max<i:
        max = i
    i+=i
print(max)