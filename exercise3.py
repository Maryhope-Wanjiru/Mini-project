average = 72.5

if average >= 70:
    print("Grade: A")
elif average >= 60:
    print("Grade: B")
elif average >= 50:
    print("Grade: C")
else:
    print("Grade: F")

if average >= 70:
    result = "Distinction"
elif average >= 50:
    result = "Pass"
else:
    result = "Fail"
print("Result:", result)