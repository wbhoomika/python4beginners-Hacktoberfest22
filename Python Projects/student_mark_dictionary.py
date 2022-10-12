n=int(input("Enter the Num of students :"))
student={"Name":[],"Mark1":[],"Mark2":[],"Mark3":[]}
for i in range(n):
    studname=input("Whats your name: ")
    stdmark1=int(input("Enter M1:"))
    stdmark2=int(input("Enter M2:"))
    stdmark3=int(input("Enter M3:"))
    student["Name"].append(studname)
    student["Mark1"].append(stdmark1)
    student["Mark2"].append(stdmark2)
    student["Mark3"].append(stdmark3)
##print(student)
##print(len(student["Name"]))
for i in range (n):
    print("**********************")
    print("Name :",student["Name"][i],"\nMark1:",student["Mark1"][i],"\nMark2",student["Mark2"][i],"\nMark3",student["Mark3"][i],"\nTotal",student["Mark1"][i]+student["Mark2"][i]+student["Mark3"][i])
    print("**********************")
nme=input("Enter the name to search:")
for i in range(n):
    if(nme==student["Name"][i]):
        print("Name found at",i+1,"position:",nme)
    else:
        print("Not found")
