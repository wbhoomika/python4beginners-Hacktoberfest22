n=int(input("Enter the Limit"))
i=1
student={"Name":[],"Class":[],"Mark":[]}
while(i<=n):
 studname=input("Enter the stud name :")
 studclass=input("Enter the class :")
 studmark=input("Enter the mark :")
 student["Name"].append(studname)
 student["Class"].append(studclass)
 student["Mark"].append(studmark)
 i=i+1
###print(len(student["Name"]))
print("Name\t\tClass\t\tMark")
print("*****************************************************")
for i in range(n):
    print(student["Name"][i],"\t",student["Class"][i],"\t",student["Mark"][i])
print("*****************************************************")
