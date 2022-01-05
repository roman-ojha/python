# Q) Write a program to calculate CGPA using marks of three subjects (out of 100)


while True:
    print("Enter the mark of the given subject:")
    math=int(input("Math: "))
    physic=int(input("Physic: "))
    chemistry=int(input("Chemistry: "))

    totalMark=(math+physic+chemistry)/3
    Grade=""

    if totalMark>=90 and totalMark<=100:
        Grade="A+"
    elif totalMark>=85 and totalMark<90:
        Grade="A"
    elif totalMark>=80 and totalMark<85:
        Grade="A-"
    elif totalMark>=77 and totalMark<80:
        Grade="B+"
    elif totalMark>=73 and totalMark<77:
        Grade="B"
    elif totalMark>=70 and totalMark<73:
        Grade="B-"
    elif totalMark>=67 and totalMark<70:
        Grade="C+"
    elif totalMark>=63 and totalMark<67:
        Grade="C"
    elif totalMark>=60 and totalMark<63:
        Grade="C-"
    elif totalMark>=55 and totalMark<60:
        Grade="D+"
    elif totalMark>=50 and totalMark<55:
        Grade="D"
    elif totalMark>=0 and totalMark<50:
        Grade="F"
    else:
        Grade="Invalid"

    if Grade is "Invalid":
        print("\nInvalid given marks plese try to input Valid marks:")
    else:
        print("\nGrade of the given mark is:\nGrade: ",Grade)
        break


