def calculate_average(marks):
    return sum(marks) / len(marks)

def classify_result(average):
    if average >= 70:
        return "Distinction"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"