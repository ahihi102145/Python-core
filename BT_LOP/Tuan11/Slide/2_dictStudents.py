students=[]

def add_student():
    masv= input("Enter the masv to add: ")
    name = input("Enter the name: ")
    age = input("Enter the age: ")
    cls = input("Enter the class: ")
    student = {
        "masv":masv,
        "name":name,
        "age":age,
        "class":cls,
    }
    students.append(student)
    print("Student added successfully!\n")

def remove_student():
    masv= input("Enter the masv to remove: ")

    for s in students:
        if s["masv"] == masv:
            students.remove(s)
            print("Student removed successfully!\n")
            return
    print("Student not found!\n")

def update_student():

    masv= input("Enter the masv to update: ")
    for s in students:
        if s["masv"] == masv:
            print("Enter new information student:")
            name = input("Enter the name: ")
            age = input("Enter the age: ")
            cls = input("Enter the class: ")
            if name:
                s["name"] = name
            if age:
                s["age"] = age
            if cls:
                s["class"] = cls

            print("Student updated successfully!\n")
            return


def find_student():
    masv =input("Enter the masv to find: ")
    for s in students:
        if s["masv"] == masv:
            print("Student found successfully!\n")
            return


def sort_student():
    print("\nsort students by name")
    students.sort(key=lambda s: s["name"])
    print("Sorted successfully.\n")

def print_student():
    print("\nStudent List")
    if not students:
        print("List is empty.\n")
        return

    for sv in students:
        print(f'{sv["masv"]} - {sv["name"]} - {sv["age"]} - {sv["class"]}')
    print()
while True:
    print("\nSTUDENT MANAGEMENT")
    print("1. Add student")
    print("2. Remove student")
    print("3. Update student")
    print("4. Find student")
    print("5. Sort student list")
    print("6. Print student list")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        remove_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        find_student()
    elif choice == "5":
        sort_student()
    elif choice == "6":
        print_student()
    elif choice == "0":
        print("Exit program.")
        break
    else:
        print("Invalid choice! Try again.\n")