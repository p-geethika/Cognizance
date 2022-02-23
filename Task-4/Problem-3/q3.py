# PROGRAM TO CREATE A 2D LIST CONSISTING OF STUDENT DETAILS AND DISPLAYING THEM

L = []
n = int(input("Enter no. of student records to be inserted in 2D List:"))
for i in range(n):
    roll  = int(input("Enter Roll No. Of Student:"))
    sname = input("Enter Name of Student:")
    marks = int(input("Enter Marks of Student:"))
    L.append([roll, sname, marks])

print()
print("Displaying Student Records")
print("Roll No\t\t Name\t\t Marks")
for i in L:
    print(i[0], "\t\t\t", i[1], "\t\t", i[2])

# PROGRAM TO DISPLAY THE 2ND RECORD/ROW FROM THE CREATED 2D LIST

print()
print("Printing 2nd record from 2D List")
print("Roll No\t\t Name\t\t Marks")
for i in range(len(L)):
    if i == 1:
        print(L[i][0], "\t\t\t", L[i][1], "\t\t", L[i][2])

