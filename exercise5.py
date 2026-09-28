def calculate_average(marks):
    return sum(marks) / len(marks)

def classify_result(average):
    if average >= 70:
        return "Distinction"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"

def main():
    marks = [65, 72, 58, 80, 49]
    average = calculate_average(marks)
    result = classify_result(average)
    print("Marks:", marks)
    print("Average:", average)
    print("Result:", result)

if __name__ == "__main__":
    main()