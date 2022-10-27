x=[]
x1=[1,2,3]
x2=[4,5,6]
x.append(x1)
x.append(x2)
print(x)
y=[]
y=x1+x2
print(y)
print(x[1][0])
del(x[1][0])
print(x)
x1.remove(2);
print(x1)
print(x)
print(len(x))
print(len(x1))
print(len(x2))
#to print the list
for i in range(len(x2)):
    print(x2[i], end=" ")
for d in x2:
    print(d, end=" ")
#else like this
print(x2)
