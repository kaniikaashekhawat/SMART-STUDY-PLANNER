def get_subject_details(i):
    print("\nSubject", i + 1)

    sub = input("Enter subject name: ")

    while True:
        dif = input("Difficulty (easy/medium/hard): ").lower()

        if dif == "easy" or dif == "medium" or dif == "hard":
            break
        else:
            print("Invalid difficulty. Please enter easy, medium or hard.")

    days = int(input("Days left for exam: "))

    return sub, dif, days 
