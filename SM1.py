def add_student():
    f=open ("student management.txt","a")
    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    marks = input("Enter Marks: ")
    f.write(sid + "," + name + "," + marks + "\n")
    f.close()
    print("✅ Student added successfully")


def view_student():
    try:
        f = open("student management.txt", "r")
    
        print("\nID\tName\tMarks")
        print("-----------------------")
        for line in f:
            line = line.strip()
            if not line:
                continue
            data=line.split(",")
            if len(data)!=3:
                continue
            sid=data[0]
            name=data[1]
            marks=data[2]
            print(sid, "\t", name, "\t", marks)
        f.close()
    except FileNotFoundError:
        print("❌ No records found")

           
    except FileNotFoundError:
        print("❌ No records found")

def search_student():
    sid=input("enter student  ID to search")
    found=False
    try:
        f=open("student management.txt","r")
        for line in f:
            data=line.strip().split(",")
            if data[0]==sid:
                print("student found:")
                print("ID:",data[0])
                print("Name",data[1])
                print("marks",data[2])
                found=True
                break
        f.close()
        if not found:
            print("student not found")
    except FileNotFoundError:
        print("no records found")

def update_student():
    sid=input("enter student ID to update:")
    updated=False
    students=[]
    try:
        f=open("student management.txt","r")
        students=f.readlines()
        f.close()

        f=open("student management.txt","w")
        for line in students:
            data=line.strip().split(",")
            if data[0]==sid:
                name=input("enter new name:")
                marks=input("enter new marks:")
                f.write(sid+","+name+","+marks+"\n")
                updated=True
            else:
                f.write(line)
        f.close()
        if updated:
            print("student updated succesfully ")
        else:
            print("student not found")
            f.write(line)
    except FileNotFoundError:
        print("no records found")



def delete_student():
    sid=input("enter student ID to delete:")
    deleted=False
    students=[]

    try:
        f=open("student management.txt","r")
        students=f.readlines()
        f.close()

        f=open("student management.txt","w")
        for line in students:
            data=line.strip().split(",")
            if data[0]==sid:
                deleted=True
            else:
                f.write(line)
        f.close()

        if deleted:
            print("student deleted succesfully")
        else:
            print("student not found")
    except FileNotFoundError:
        print("no records found")



while True:
    print("\n====Student management system:=======")
    print("1.add student:")
    print("2.view student:")
    print("3.search student:")
    print("4.update student:")
    print("5.delete student:")
    print("6.exit:")

    choice=input("enter your choice:")
    if choice=="1":
        add_student()
    elif choice=="2":
        view_student()
    elif choice=="3":
        search_student()
    elif choice=="4":
        update_student()
    elif choice=="5":
        delete_student()
    elif choice=="6":
        print("exiting program;")
        break
    else:
        print("invalid choice")
    