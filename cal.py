English_marks = int(input("Enter English marks: "))
Kiswahili_marks  = int(input("Enter Kiswahili marks: "))
Maths_marks = int(input("Enter Maths marks: "))
Biology_marks = int(input("Enter Biology marks: "))
Chemistry_marks =int(input("Enter Chemistry marks: "))

total_marks = English_marks + Kiswahili_marks + Maths_marks + Biology_marks + Chemistry_marks
Average_marks = total_marks / 5

if Average_marks >= 80:
    print("Grade A")
elif Average_marks >= 70:
    print("Grade B")
elif Average_marks >= 60:
    print("Grade C")
elif Average_marks >= 50:
    print("Grade D")
else:
    print("Grade F")    