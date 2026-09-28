from grading_utils import calculate_average, classify_result

def main():
    name = input("Student name: ")
    mark1 = float(input("Mark for unit 1: "))
    mark2 = float(input("Mark for unit 2: "))
    mark3 = float(input("Mark for unit 3: "))

    average = calculate_average([mark1, mark2, mark3])
    result = classify_result(average)

    print()
    print("----- RESULT SUMMARY -----")
    print("Student:", name)
    print("Marks:", mark1, mark2, mark3)
    print("Average:", round(average, 2))
    print("Result:", result)

if __name__ == "__main__":
    main()