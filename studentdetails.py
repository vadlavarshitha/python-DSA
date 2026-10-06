print("STUDENT MARKS SYSTEM")
print("--------------------")

name = input("Enter student name: ")
roll = input("Enter roll number: ")

m1 = int(input("Enter Maths marks: "))
m2 = int(input("Enter Physics marks: "))
m3 = int(input("Enter Chemistry marks: "))
m4 = int(input("Enter Python marks: "))
m5 = int(input("Enter English marks: "))

total = m1 + m2 + m3 + m4 + m5
percentage = total / 5

print("\n--- RESULT ---")
print("Name:", name)
print("Roll Number:", roll)
print("Maths:", m1)
print("Physics:", m2)
print("Chemistry:", m3)
print("Python:", m4)
print("English:", m5)

print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 70:
    grade = "B"
elif percentage >= 60:
    grade = "C"
elif percentage >= 50:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)

if percentage >= 40:
    print("Result: PASS")
else:
    print("Result: FAIL")

print("--------------------")
print("Thank You")