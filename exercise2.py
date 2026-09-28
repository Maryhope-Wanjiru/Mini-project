mark1 = 65
mark2 = 72
mark3 = 58

total = mark1 + mark2 + mark3
average = total / 3
print("Total:", total)
print("Average:", average)

pass_mark = 50
print("Average is a pass:", average >= pass_mark)

meets_pass = average >= pass_mark and mark1 >= 40 and mark2 >= 40 and mark3 >= 40
print("Meets pass condition:", meets_pass)