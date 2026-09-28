import grading_utils

marks = [65, 72, 58, 80, 49]
average = grading_utils.calculate_average(marks)
result = grading_utils.classify_result(average)

print("Average:", average)
print("Result:", result)