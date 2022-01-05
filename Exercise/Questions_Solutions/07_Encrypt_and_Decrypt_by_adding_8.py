# Q) Write a program to encrypt a grade by adding 8 to it. Decrypt it to show the correct grade.


def calculateGrade(totalMark):
    if totalMark>=90 and totalMark<=100:
        return "A+"
    elif totalMark>=85 and totalMark<90:
        return "A"
    elif totalMark>=80 and totalMark<85:
        return "A-"
    elif totalMark>=77 and totalMark<80:
        return "B+"
    elif totalMark>=73 and totalMark<77:
        return "B"
    elif totalMark>=70 and totalMark<73:
        return "B-"
    elif totalMark>=67 and totalMark<70:
        return "C+"
    elif totalMark>=63 and totalMark<67:
        return "C"
    elif totalMark>=60 and totalMark<63:
        return "C-"
    elif totalMark>=55 and totalMark<60:
        return "D+"
    elif totalMark>=50 and totalMark<55:
        return "D"
    elif totalMark>=0 and totalMark<50:
        return "F"
    else:
        return "Invalid"

print("Enter the mark of the given subject:")
math=int(input("Math: "))
physic=int(input("Physic: "))
chemistry=int(input("Chemistry: "))

totalMark=(math+physic+chemistry)/3
encryptedMarks=totalMark+8

Grade=calculateGrade(encryptedMarks)
print("Encrypted grade: ",Grade)
print("Decrypted grade: ",calculateGrade(encryptedMarks-8))
