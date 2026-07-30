classmates=["arif","priya","rahul","muhammad","benji"]
print("calss list",classmates)

print("total students",len(classmates))
print("first student",classmates[0])
print("last student",classmates[-1])
print("first three students",classmates[:3])
classmates.append("jhon")
print("afteradding jhon",classmates)
classmates.remove("rahul")
print("after removing rahul",classmates)
classmates.sort()
print("sorted alphabetically",classmates)
classmates.reverse()
print("revese",classmates)

teacher={"name":"mr sharma","subject":"computers","experience":"8"}
print("teacher profile",teacher)

print("subject",teacher["subject"])
print("experience",teacher.get("experience","not found"))
teacher["experience"]=9
print("updated teacher profile",teacher)
teacher["email"]="sharma@school.com"
teacher.pop("experience")
print("updated teacher profile",teacher)


role_numbers=[1,2,3,4,5]
name=["benji","angel","aiden","muhammad","tyson"]
student_directory=dict(zip(role_numbers,name))
print("student directory",student_directory)
