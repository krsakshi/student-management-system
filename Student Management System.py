print("\n\nStudent Management System \n\n")

c=1         # For exiting main loop
n = []      # Name list
r = []      # Roll No list
b = []      # Branch list
p = []      # Phone No list
a = []      # Address list
g = []      # Grade list

while(c==1):      # Loop will continue until the value of c not equal to 1 (Helps in Exit choise)

    print("INSTRUCTIONS:")              # Instrunctions
    print("Press:1 To Add a Student")
    print("Press:2 To View a Student Details")
    print("Press:3 To View all Students Details")
    print("Press:4 To Delete a Student Record")
    print("Press:5 to Update Student's Info")
    print("Press:6 to Exit")

    e = int(input("\nEnter your choise : "))

    if(e==1):                   # For adding new student
        print("You choosed to Add a Student\n")

        print("Please enter the following information")
        i=input("Roll no : ")
        r.append(i)
        na=input("Student Name : ")
        n.append(na)
        br=input("Branch : ")
        b.append(br)
        ph=input("Phone Number : ")
        p.append(ph)
        ad=input("Address : ")
        a.append(ad)
        gr=input("Grade : ")
        g.append(gr)
        
        print("\nData Entered Sucessfully\n")

        print("If you want to exit then press 1")
        y=int(input("Else press 0 to return to main menu : "))
        print("\n\n")
        
        if(y==1):
            print("\nThankYou")
            break
        else:
            continue


    elif(e==2):                # For specific student details
        print("You choosed to View a Students Details \n")
        
        i = int(input("Enter roll number of student whose details you want to view : "))
        print("\nStudent Name : ", n[i-1])
        print("Roll no : ", r[i-1])
        print("Branch : ", b[i-1])
        print("Phone Number : ", p[i-1])
        print("Address : ", a[i-1])
        print("Grade :", g[i-1])
        print("\n")

        print("If you want to exit then press 1")
        y=int(input("Else press 0 to return to main menu : "))
        print("\n\n")
        
        if(y==1):
            print("\nThankYou")
            break
        else:
            continue


        
    elif(e==3):                 # For viewing all student details
        print("You choosed to View all Students Details \n")
        lr=int(input("Enter last roll number : "))
        print("\n\n")
        
        for i in range(0,lr):

            print("Student Name : ", n[i])
            print("Roll no : ", r[i])
            print("Branch : ", b[i])
            print("Phone Number : ", p[i])
            print("Address : ", a[i])
            print("Grade :", g[i])
            print("\n")

        print("If you want to exit then press 1")
        y=int(input("Else press 0 to return to main menu : "))
        print("\n\n")
        
        if(y==1):
            print("\nThankYou")
            break
        else:
            continue

    