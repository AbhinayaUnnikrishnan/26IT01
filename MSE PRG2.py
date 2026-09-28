students={}
def add_student():
    name=input("enter the name:")
    marks=float(input("enter the marks:"))
    if marks>=90:
        grade="A+"
    elif marks>=80:
        grade="A"
    elif marks>=70:
        grade="B"
    elif marks>=60:
        grade="C"
    else:
        grade="D"
    students[name]=(marks,grade)
def display_students():
    print("\n students details:")
    print("--------------------")
    for name,details in students.items():
        print("name:",name)
        print("grade:",details[1])
        print("marks:",details[0])
        print()
while True:
    print("1.add students")
    print("2.display students")
    print("3.exit")
    choice=(input("enter choice:"))
    if choice=="1":
        add_student()
    elif choice=="2":
        display_students()
    elif choice=="3":
        break
    else:
        print("invalid choice")
        
