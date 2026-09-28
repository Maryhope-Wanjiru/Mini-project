marks = [65, 72, 58, 80, 49]

for mark in marks:
    print(mark)

total = 0
for mark in marks:
    total = total + mark
average = total / len(marks)
print("Total (loop):", total)
print("Average (loop):", average)

print("Total (sum):", sum(marks))
print("Average (built-in):", sum(marks) / len(marks))