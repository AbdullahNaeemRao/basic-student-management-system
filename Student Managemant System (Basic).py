data = []

def add():
    name = input("Enter name: ")
    roll = input("Enter roll number: ")
    marks = input("Enter marks: ")
    gender = input("Enter gender (Male/Female): ")
    religion = input("Enter religion: ")
    domicile = input("Enter domicile city: ")
    dob = input("Enter date of birth (DD/MM/YYYY): ")
    department = input("Enter department: ")
    section = input("Enter section: ")
    session = input("Enter session: ")

    # Store all details in a list
    data.append([name, roll, marks, gender, religion, domicile, dob, department, section, session])
    print("Student added")

def show():
    if len(data) == 0:
        print("No record found")
    else:
        for i in data:
            print("\nName:", i[0], "\nRoll:", i[1], "\nMarks:", i[2],
                  "\nGender:", i[3], "\nReligion:", i[4], "\nDomicile:", i[5],
                  "\nDOB:", i[6], "\nDepartment:", i[7], "\nSection:", i[8], "\nSession:", i[9])

def search():
    r = input("Enter roll number to search: ")
    found = False
    for i in data:
        if i[1] == r:
            print("\nName:", i[0], "\nRoll:", i[1], "\nMarks:", i[2],
                  "\nGender:", i[3], "\nReligion:", i[4], "\nDomicile:", i[5],
                  "\nDOB:", i[6], "\nDepartment:", i[7], "\nSection:", i[8], "\nSession:", i[9])
            found = True
    if not found:
        print("Student not found")

def remove():
    r = input("Enter roll number to delete: ")
    for i in data:
        if i[1] == r:
            data.remove(i)
            print("Student removed")
            return
    print("Student not found")

while True:
    print("\n1 Add Student")
    print("2 View Students")
    print("3 Search Student")
    print("4 Delete Student")
    print("5 Exit")
    
    ch = input("Enter choice: ")

    if ch == "1":
        add()
    elif ch == "2":
        show()
    elif ch == "3":
        search()
    elif ch == "4":
        remove()
    elif ch == "5":
        break
    else:
        print("Wrong choice")
